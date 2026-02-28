import re
import glob

files = glob.glob('aulas/*.html')

# We want the standard to be:
# <title>{Lesson Name} · {Topic}</title>
# i.e., "POO na Prática · Python"
# or "Coleções & Arquivos · Python"

replacements = {
    'gh-01-primeiro-commit.html': 'Do Zero ao Primeiro Commit · GitHub',
    'gh-02-branches-merge.html': 'Branches, Merge & Conflitos · GitHub',
    'html-01-semantico-estrutura.html': 'HTML Semântico & Estrutura · HTML/CSS',
    'html-02-box-flexbox-grid.html': 'Box Model, Flexbox & Grid · HTML/CSS',
    'py-01-ambiente-primeiros-passos.html': 'Ambiente & Primeiros Passos · Python',
    'py-02-logica-funcoes.html': 'Lógica & Funções · Python',
    'py-03-colecoes-arquivos.html': 'Coleções & Arquivos · Python',
    'py-04-poo.html': 'POO na Prática · Python'
}

for filepath in files:
    filename = filepath.split('\\')[-1].split('/')[-1]
    if filename in replacements:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_title = f"<title>{replacements[filename]}</title>"
        content = re.sub(r'<title>.*?</title>', new_title, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated title in {filename}")
