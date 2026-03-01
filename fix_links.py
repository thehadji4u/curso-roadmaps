import os
import re

aulas_dir = r"p:\BACKUP\URNA\Curso Roadmaps\aulas"
roadmap_file = r"p:\BACKUP\URNA\Curso Roadmaps\roadmaps_new.html"

# Correta sequência baseada no lessons-index.md
lessons = [
    "gh-01-primeiro-commit.html",          # 0
    "gh-02-branches-merge.html",           # 1
    "html-01-semantico-estrutura.html",    # 2
    "html-02-box-flexbox-grid.html",       # 3
    "py-01-ambiente-primeiros-passos.html",# 4
    "py-02-logica-funcoes.html",           # 5
    "py-03-estruturas-dados.html",         # 6
    "py-04-orientacao-objetos.html",       # 7
    "html-03-responsivo-moderno.html",     # 8
    "html-04-animacoes-efeitos.html",      # 9
    "gh-03-colaboracao-prs.html",          # 10
    "js-01-core-dom.html"                  # 11
]

# 1. Corrigir os arquivos de aula na pasta aulas/
for i in range(10): # Apenas as 10 primeiras
    filename = lessons[i]
    filepath = os.path.join(aulas_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    prev_link = lessons[i-1] if i > 0 else "../roadmaps_new.html"
    next_link = lessons[i+1]
    
    # Substituir href="${qq coisa}" class="nav-prev"
    # Note: the class could be after or before, but Usually it's `href="..." class="nav-prev"`
    content = re.sub(r'href="[^"]*"(?=.*class="nav-prev")', f'href="{prev_link}"', content)
    # in case class is before href:
    content = re.sub(r'(class="nav-prev"[^>]*?)href="[^"]*"', rf'\1href="{prev_link}"', content)
    
    content = re.sub(r'href="[^"]*"(?=.*class="nav-next")', f'href="{next_link}"', content)
    content = re.sub(r'(class="nav-next"[^>]*?)href="[^"]*"', rf'\1href="{next_link}"', content)
    
    content = re.sub(r'href="[^"]*"(?=.*class="next-card")', f'href="{next_link}"', content)
    content = re.sub(r'(class="next-card"[^>]*?)href="[^"]*"', rf'\1href="{next_link}"', content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Updated {filename}: prev={prev_link}, next={next_link}")

print("Done updating lesson files.")
