import os
import glob
import re
from bs4 import BeautifulSoup

# Padrão das classes que NUNCA devemos remover (dynamic highlight, mermaid, etc)
ALWAYS_KEEP_CLASSES = {'language-python', 'language-html', 'language-css', 'language-javascript', 'hljs', 'mermaid'}
ALWAYS_KEEP_TAGS = {'html', 'body', '*', 'main'}

def extract_classes_from_selector(sel):
    return set(re.findall(r'\.([a-zA-Z0-9_-]+)', sel))

def process_css_rules(css_text, used_classes, used_tags):
    """
    Processa um bloco de regras CSS onde não há nested braces (como dentro de @media ou raiz)
    """
    # Ex: .hero, .hero-eyebrow { ... }
    # Vamos usar um regex mais seguro que não tenta matchar chaves aninhadas.
    # Mas sabendo que não há chaves aninhadas aqui.
    rule_pattern = r'([^{}]+)\{([^{}]*)\}'
    
    new_css = ""
    for match in re.finditer(rule_pattern, css_text):
        selectors_raw = match.group(1).strip()
        body = match.group(2)
        
        if selectors_raw.startswith("/*"):
            # skip a protected block marker or just comments?
            if "PROTECTED_" in selectors_raw or "MEDIA_" in selectors_raw:
                new_css += match.group(0) + "\n"
                continue
        
        # Split por vírgula para processar cada seletor
        selectors = [s.strip() for s in selectors_raw.split(',') if s.strip()]
        kept_selectors = []
        
        for sel in selectors:
            # limpar pseudo (ex: :hover, ::before)
            clean_sel = re.sub(r':.*', '', sel)
            
            sel_classes = extract_classes_from_selector(clean_sel)
            # se ele exigir uma classe que não temos, descartamos
            if sel_classes:
                if all(c in used_classes or any(c.startswith(a) for a in ['hljs', 'language']) for c in sel_classes):
                    # Todas as classes requeridas existem, ou é hljs/lang
                    kept_selectors.append(sel)
            else:
                # se não tem classe (ex: p, h1, body)
                # mantemos se a tag existe, ou é uma das padrão
                tags = set(re.findall(r'(?<![.#-])\b([a-zA-Z0-9]+)\b', clean_sel))
                if not tags or any(t.lower() in used_tags or t.lower() in ALWAYS_KEEP_TAGS for t in tags):
                    kept_selectors.append(sel)
                    
        if kept_selectors:
            new_css += ", ".join(kept_selectors) + " {" + body + "}\n"
            
    return new_css

def purge_css(html_path):
    print(f"Limpando CSS para: {html_path}")
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    used_classes = set()
    used_tags = set([tag.name.lower() for tag in soup.find_all()])
    
    for tag in soup.find_all(True):
        if tag.get('class'):
            used_classes.update(tag.get('class'))
            
    # Tem que achar o bloco <style> grande (injecao do lesson.css)
    # Tem um bloco TOKENS no topo e depois as regras...
    # Vamos focar no estilo principal
    style_blocks = re.findall(r'<style>(.*?)</style>', html, flags=re.DOTALL)
    
    if not style_blocks:
        return
        
    for i, css_content in enumerate(style_blocks):
        # Se for o root variables apenas, pule
        if "TOKENS" in css_content and "/* ─── RESET" not in css_content:
            continue
            
        # Passo 1: Limpar comentários reais (não os markers)
        # Importante: precisamos tomar cuidado com chaves aninhadas!
        css = css_content
        
        # Proteger @import
        imports = []
        for imp in re.finditer(r'@import[^;]+;', css):
            imports.append(imp.group(0))
            css = css.replace(imp.group(0), f"/*IMP_{len(imports)-1}*/")
            
        # Proteger @keyframes
        keyframes = []
        # Keyframes tem animações com 0% {} 100% {} -> chaves aninhadas!
        for kf in re.finditer(r'@keyframes\s+[^{]+\s*\{\s*(?:[^{}]*\{[^{}]*\}[^{}]*)*\s*\}', css):
            keyframes.append(kf.group(0))
            css = css.replace(kf.group(0), f"/*KF_{len(keyframes)-1}*/")
            
        # Proteger :root (aninhamento não tem, mas var --x: y;)
        roots = []
        for r in re.finditer(r':root\s*\{[^{}]*\}', css):
            roots.append(r.group(0))
            css = css.replace(r.group(0), f"/*ROOT_{len(roots)-1}*/")
            
        # Proteger media query
        medias = []
        # Pode ter propriedades dentro do media
        for mq in re.finditer(r'@media\s*[^{]+\{\s*((?:[^{}]*\{[^{}]*\}[^{}]*)*)\s*\}', css):
            mq_full = mq.group(0)
            mq_inner = mq.group(1)
            # Processar o inner
            new_inner = process_css_rules(mq_inner, used_classes, used_tags)
            if new_inner.strip():
                # recriar media query
                head = re.match(r'@media\s*[^{]+\{', mq_full).group(0)
                new_mq = head + "\n" + new_inner + "\n}"
            else:
                new_mq = ""
                
            medias.append(new_mq)
            css = css.replace(mq_full, f"/*MQ_{len(medias)-1}*/")
            
        # Agora o resto são regras de 1 nível de bloco
        final_css_1 = process_css_rules(css, used_classes, used_tags)
        
        # Restaurar
        for idx, imp in enumerate(imports):
            final_css_1 = final_css_1.replace(f"/*IMP_{idx}*/", imp)
        for idx, kf in enumerate(keyframes):
            final_css_1 = final_css_1.replace(f"/*KF_{idx}*/", kf)
        for idx, rt in enumerate(roots):
            final_css_1 = final_css_1.replace(f"/*ROOT_{idx}*/", rt)
        for idx, mq in enumerate(medias):
            final_css_1 = final_css_1.replace(f"/*MQ_{idx}*/", mq)
            
        final_css_1 = final_css_1.strip()
        
        # Substituir bloco do HTML
        html = html.replace(f"<style>{css_content}</style>", f"<style>\n{final_css_1}\n</style>")
        
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    for f in glob.glob('aulas/*.html'):
        purge_css(f)
    print("Purge finalizado para todos os arquivos!")
