import glob
import re

print("Carregando lesson.css...")
with open("assets/css/lesson.css", "r", encoding="utf-8") as f:
    css_content = f.read()

# Construir bloco style em formato HTML
style_block = f"\n  <style>\n{css_content}\n  </style>\n"

count = 0
for filepath in glob.glob("aulas/*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Substituir o link do lesson.css pelo bloco de estilo embutido
    # Ex: <link rel="stylesheet" href="../assets/css/lesson.css">
    pattern = r'<link[^>]*href="\.\./assets/css/lesson\.css"[^>]*>'
    
    if re.search(pattern, html):
        new_html = re.sub(pattern, lambda m: style_block, html)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"✅ Estilos embutidos em: {filepath}")
        count += 1
    else:
        # Se não achar a tag, pode já estar embutido ou usar outro caminho
        if "lesson.css" not in html and "<style>" in html:
            print(f"⚠️ Estilos possivelmente já embutidos em: {filepath}")
        else:
            print(f"❌ Não encontrou a tag link do lesson.css em: {filepath}")

print(f"\nConcluído! {count} arquivos atualizados.")
