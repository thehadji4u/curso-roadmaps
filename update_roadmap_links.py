import re
import os

roadmap_path = 'p:\\BACKUP\\URNA\\Curso Roadmaps\\roadmaps_new.html'

with open(roadmap_path, 'r', encoding='utf-8') as f:
    html = f.read()

lessons = [
    ("Git — Do zero ao primeiro commit", "aulas/gh-01-primeiro-commit.html", "github-theme-link"),
    ("Git — Branches, Merge & Conflitos", "aulas/gh-02-branches-merge.html", "github-theme-link"),
    ("HTML Semântico & Estrutura", "aulas/html-01-semantico-estrutura.html", "html-theme-link"),
    ("CSS — Box Model, Flexbox & Grid", "aulas/html-02-box-flexbox-grid.html", "html-theme-link"),
    ("Python — Ambiente & Primeiros Passos", "aulas/py-01-ambiente-primeiros-passos.html", "python-theme-link"),
    ("Python — Lógica & Funções", "aulas/py-02-logica-funcoes.html", "python-theme-link"),
    ("Python — Estruturas de Dados", "aulas/py-03-estruturas-dados.html", "python-theme-link"),
    ("Python — Orientação a Objetos", "aulas/py-04-orientacao-objetos.html", "python-theme-link"),
    ("CSS — Responsivo & Moderno", "aulas/html-03-responsivo-moderno.html", "html-theme-link"),
    ("CSS — Animações, Tipografia & Efeitos", "aulas/html-04-animacoes-efeitos.html", "html-theme-link")
]

for title, href, theme_class in lessons:
    # Caso 1: Já é um <a ...>, mas o href pode estar errado ou o theme_class.
    # Pattern para achar a tag inteira que termina em </a> e contém o title
    pattern_a = r'<a href="[^"]*" class="item[^"]*"(>\s*<div class="item-title">\s*' + re.escape(title) + r'.*?</a>)'
    match_a = re.search(pattern_a, html, re.DOTALL)
    
    if match_a:
        # Substitui a abertura da tag a
        new_a = f'<a href="{href}" class="item {theme_class}"' + match_a.group(1)
        html = html[:match_a.start()] + new_a + html[match_a.end():]
        print(f"Updated existing <a> for: {title}")
        continue
        
    # Caso 2: É um <div class="item"> que precisamos embrulhar num <a href="">...</a>
    pattern_div = r'(<div class="item[^"]*">\s*<div class="item-title">\s*' + re.escape(title) + r'.*?</div>\s*</div>)'
    match_div = re.search(pattern_div, html, re.DOTALL)
    
    if match_div:
        inner_content = match_div.group(1)
        # Substitui o '<div class="item...">' no conteúdo pelo interior da div original
        # The easiest way is to change the outer <div class="item..."> to <a href="" class="..."> and the closing </div> to </a>
        # Let's extract everything inside the <div class="item..."> ... </div>
        # A regex for inner is simple since we matched the whole block
        inner_match = re.search(r'<div class="item[^"]*">(.*)</div>', inner_content, re.DOTALL)
        if inner_match:
            new_block = f'<a href="{href}" class="item {theme_class}">{inner_match.group(1)}</a>'
            html = html[:match_div.start()] + new_block + html[match_div.end():]
            print(f"Wrapped <div> in <a> for: {title}")
        else:
            print(f"Could not parse inner div for: {title}")
        continue
        
    print(f"Could not find title: {title}")

with open(roadmap_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done updating roadmaps_new.html.")
