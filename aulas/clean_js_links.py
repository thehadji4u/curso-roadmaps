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
    "js-01-core-dom.html": "JavaScript — Core & DOM",
    "js-02-objetos-es6.html": "JavaScript — Objetos & ES6",
    "js-03-async-promises.html": "JavaScript — Async & Promises"
}

def fix_js_footers():
    for f in ["js-01-core-dom.html", "js-02-objetos-es6.html", "js-03-async-promises.html"]:
        path = f'p:/BACKUP/URNA/Curso Roadmaps/aulas/{f}'
        if not os.path.exists(path):
            continue
            
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Get next file
        idx = SEQUENCE.index(f)
        if idx == len(SEQUENCE) - 1:
            continue
        
        next_file = SEQUENCE[idx + 1]
        next_title = TITLES.get(next_file, "")
        if not next_title:
            # We already updated titles map in the first script, but let's just extract it again here if needed
            # wait, I already hardcoded TITLES above for JS
            pass
            
        # The structure is:
        # <div class="next-card">
        #   <div class="next-card-info">
        #     <div class="next-label">PRÓXIMA AULA • ⚡ JavaScript</div>
        #     <h3>Objetos, Arrays & ES6+</h3>
        #     ...
        #   </div>
        #   <a href="js-02-objetos-es6.html" class="next-btn">Próxima aula →</a>
        # </div>
        
        # 1. Fix the link
        content = re.sub(r'<a\s+href="[^"]*"\s+class="next-btn"', f'<a href="{next_file}" class="next-btn"', content)
        
        # 2. Fix the title in <h3>
        content = re.sub(r'<div class="next-label">([^<]*)</div>\s*<h3>([^<]*)</h3>', 
                         f'<div class="next-label">PRÓXIMA AULA • ⚡ JavaScript</div>\\n          <h3>{next_title}</h3>', 
                         content)
                         
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)

if __name__ == '__main__':
    fix_js_footers()
    print("JS footers fixed.")
