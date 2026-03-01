import os
import re
import json

FILES = [
    "gh-01-primeiro-commit.html",
    "gh-02-branches-merge.html",
    "gh-03-colaboracao-prs.html",
    "js-01-core-dom.html",
    "js-02-objetos-es6.html",
    "js-03-async-promises.html"
]

data = {}
for f in FILES:
    path = f'p:/BACKUP/URNA/Curso Roadmaps/aulas/{f}'
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    matches = re.finditer(r'<div class="section-label">(.*?)</div>', content)
    data[f] = [m.group(1) for m in matches]
    
with open('p:/BACKUP/URNA/Curso Roadmaps/aulas/headers_dump.json', 'w', encoding='utf-8') as out:
    json.dump(data, out, indent=2, ensure_ascii=False)
