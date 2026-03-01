import re
import os

roadmap_path = 'p:\\BACKUP\\URNA\\Curso Roadmaps\\roadmaps_new.html'

with open(roadmap_path, 'r', encoding='utf-8') as f:
    html = f.read()

titles = re.findall(r'<div class="item-title">(.*?)</div>', html, re.DOTALL)
for i, t in enumerate(titles):
    # strip spans to read just text
    text_only = re.sub(r'<[^>]+>', '', t).strip()
    print(f"{i}: {text_only}")
