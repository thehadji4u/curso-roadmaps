import re

roadmap_path = 'p:\\BACKUP\\URNA\\Curso Roadmaps\\roadmaps_new.html'

with open(roadmap_path, 'r', encoding='utf-8') as f:
    html = f.read()

aula_map = {
    "01": ("aulas/gh-01-primeiro-commit.html", "github-theme-link"),
    "02": ("aulas/gh-02-branches-merge.html", "github-theme-link"),
    "03": ("aulas/html-01-semantico-estrutura.html", "html-theme-link"),
    "04": ("aulas/html-02-box-flexbox-grid.html", "html-theme-link"),
    "05": ("aulas/py-01-ambiente-primeiros-passos.html", "python-theme-link"),
    "06": ("aulas/py-02-logica-funcoes.html", "python-theme-link"),
    "07": ("aulas/py-03-estruturas-dados.html", "python-theme-link"),
    "08": ("aulas/py-04-orientacao-objetos.html", "python-theme-link"),
    "09": ("aulas/html-03-responsivo-moderno.html", "html-theme-link"),
    "10": ("aulas/html-04-animacoes-efeitos.html", "html-theme-link")
}

# The regex looks for <div or <a class="item..."> then an item-title containing ▶ Aula XX, then item-desc, then closing </div or </a
pattern = r'<(div|a)([^>]*)class="item([^"]*)"([^>]*)>(\s*<div class="item-title">.*?▶\s*Aula\s*(\d{2}).*?</div>\s*<div class="item-desc">.*?</div>\s*)</\1>'

count_modified = 0

def replace_item(match):
    global count_modified
    tag = match.group(1)
    attrs_before = match.group(2)
    cls = match.group(3)
    attrs_after = match.group(4)
    inner = match.group(5)
    aula_num = match.group(6)
    
    if aula_num not in aula_map:
        return match.group(0)
        
    href, theme_class = aula_map[aula_num]
    
    # Clean cls
    clean_cls = cls.replace('github-theme-link', '').replace('html-theme-link', '').replace('python-theme-link', '')
    if theme_class not in clean_cls:
        new_cls = clean_cls + ' ' + theme_class
    else:
        new_cls = clean_cls
        
    # Remove existing href
    import re as regex
    attrs_before = regex.sub(r'\s*href="[^"]*"', '', attrs_before)
    attrs_after = regex.sub(r'\s*href="[^"]*"', '', attrs_after)
    
    # We guarantee we produce an <a> tag
    new_tag = f'<a href="{href}"{attrs_before}class="item{new_cls}"{attrs_after}>{inner}</a>'
    count_modified += 1
    return new_tag

new_html = re.sub(pattern, replace_item, html, flags=re.DOTALL)

with open(roadmap_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"Finished updating roadmap loops! Modified {count_modified} items.")
