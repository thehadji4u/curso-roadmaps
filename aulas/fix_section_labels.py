import re
import os

FILES_TO_FIX = [
    "gh-01-primeiro-commit.html",
    "gh-02-branches-merge.html",
    "gh-03-colaboracao-prs.html",
    "js-01-core-dom.html",
    "js-02-objetos-es6.html",
    "js-03-async-promises.html"
]

def clean_label(text):
    # If it's already '// próximos passos' or similar, we might want to just make it uppercase
    # Remove leading '// ' if exists
    text = re.sub(r'^//\s*', '', text)
    
    # Remove leading digits and separators like '-', '—', '·', '.'
    text = re.sub(r'^\d+\s*[-—·\.]\s*', '', text)
    
    # Uppercase
    text = text.upper()
    
    return f"// {text}"

for f in FILES_TO_FIX:
    path = f'p:/BACKUP/URNA/Curso Roadmaps/aulas/{f}'
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    def replacer(match):
        original = match.group(1)
        cleaned = clean_label(original)
        return f'<div class="section-label">{cleaned}</div>'
        
    new_content = re.sub(r'<div class="section-label">(.*?)</div>', replacer, content)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
    else:
        print(f"No changes for {f}")
