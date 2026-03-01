import glob
import re
import os

SEQUENCE = [
    "html-01-semantico-estrutura.html",
    "html-02-box-flexbox-grid.html",
    "py-01-ambiente-primeiros-passos.html",
    "py-02-logica-funcoes.html",
    "py-03-estruturas-dados.html",
    "py-04-orientacao-objetos.html",
    "html-03-responsivo-moderno.html",
    "html-04-animacoes-efeitos.html",
    "gh-01-primeiro-commit.html",
    "gh-02-branches-merge.html",
    "gh-03-colaboracao-prs.html",
    "js-01-core-dom.html",
    "js-02-objetos-es6.html",
    "js-03-async-promises.html"
]

TITLES = {
    "html-01-semantico-estrutura.html": "HTML Semântico & Estrutura",
    "html-02-box-flexbox-grid.html": "CSS — Box Model, Flexbox & Grid",
    "py-01-ambiente-primeiros-passos.html": "Python — Ambiente & Primeiros Passos",
    "py-02-logica-funcoes.html": "Python — Lógica & Funções",
    "py-03-estruturas-dados.html": "Python — Estruturas de Dados",
    "py-04-orientacao-objetos.html": "Python — Orientação a Objetos",
    "html-03-responsivo-moderno.html": "CSS — Responsivo & Moderno",
    "html-04-animacoes-efeitos.html": "CSS — Animações & Efeitos",  # or similar
    "gh-01-primeiro-commit.html": "Git — Primeiro Commit",
    "gh-02-branches-merge.html": "Git — Branches & Merge",
    "gh-03-colaboracao-prs.html": "GitHub — Colaboração & Pull Requests",
    "js-01-core-dom.html": "JavaScript — Core & DOM",
    "js-02-objetos-es6.html": "JavaScript — Objetos & ES6",
    "js-03-async-promises.html": "JavaScript — Async & Promises"
}

TOPICS = {
    "html": "🌐 HTML/CSS",
    "py": "🐍 Python",
    "gh": "🐙 GitHub",
    "js": "⚡ JavaScript"
}

# Find titles dynamically to be sure:
for f in SEQUENCE:
    path = f'p:/BACKUP/URNA/Curso Roadmaps/aulas/{f}'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            c = file.read()
            # usually in <title> ou <h1>
            m = re.search(r'<title>(.*?)</title>', c)
            if m:
                # e.g., "Aula 01 — HTML Semântico"
                title = m.group(1).split("—")[-1].strip()
                if "Aula" not in title:
                    # just keep the whole string if no "—"
                    pass
                # Better: get the <h1>
                m2 = re.search(r'<h1>(.*?)</h1>', c)
                if m2:
                    TITLES[f] = m2.group(1).replace("<br>", " ").strip()

def get_topic(filename):
    prefix = filename.split('-')[0]
    return TOPICS.get(prefix, "Módulo")

def update_all_footers():
    for i, current_file in enumerate(SEQUENCE):
        if i == len(SEQUENCE) - 1:
            break # last file, no next lesson
            
        next_file = SEQUENCE[i + 1]
        next_title = TITLES[next_file]
        next_topic = get_topic(next_file)
        
        # update current_file
        path = f'p:/BACKUP/URNA/Curso Roadmaps/aulas/{current_file}'
        if not os.path.exists(path):
            continue
            
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # We need to replace:
        # <a href="..." class="next-card">...</a>
        # Using regex to target the whole <a> tag for the next card
        
        # First, ensure we get the right href
        def regex_replacer(match):
            href_attr = match.group(1) # e.g. href="html-02.html"
            classes = match.group(2) # e.g. class="next-card"
            inner = match.group(3)
            
            # Sub-replace inside inner
            # <div class="next-card-label">PRÓXIMA AULA • Tema</div>
            inner = re.sub(r'<div class="([^"]*label[^"]*)">.*?</div>', 
                           f'<div class="\\1">PRÓXIMA AULA • {next_topic}</div>', inner)
            inner = re.sub(r'<div class="([^"]*title[^"]*)">.*?</div>', 
                           f'<div class="\\1">{next_title}</div>', inner)
            
            return f'<a href="{next_file}"{classes}>{inner}</a>'
        
        new_content = re.sub(r'<a\s+href="([^"]*)"([^>]*(?:next-card|next-lesson-card)[^>]*)>(.*?)</a>', 
                             regex_replacer, content, flags=re.DOTALL)
                             
        
        with open(path, 'w', encoding='utf-8') as file:
            file.write(new_content)

if __name__ == '__main__':
    update_all_footers()
    print("Done standardizing titles and links.")
