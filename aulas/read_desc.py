import glob
import re
import os
import json

data = {}
files = glob.glob('p:/BACKUP/URNA/Curso Roadmaps/aulas/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    p_text = ""
    next_title = ""
    # Look for <h2>O que vem a seguir?</h2> followed by a <p>
    match = re.search(r'<h2>O que vem a seguir\?.*?</h2>\s*(<p.*?>.*?</p>)\s*<a .*?(?:next-card|next-lesson-card|next-steps-card).*?>\s*<div>\s*<div.*?>.*?</div>\s*<div.*?>\s*(.*?)\s*</div>', content, re.DOTALL | re.IGNORECASE)
    
    if match:
        p_text = match.group(1).strip()
        next_title = match.group(2).strip()
    else:
        # Fallback to general finding
        match2 = re.search(r'<h2>O que vem a seguir\?.*?</h2>.*?(<p.*?>.*?</p>).*?class="(?:next-title|next-card-title)">(.*?)</div>', content, re.DOTALL | re.IGNORECASE)
        if match2:
            p_text = match2.group(1).strip()
            next_title = match2.group(2).strip()

    data[os.path.basename(f)] = {
        "next_title": next_title,
        "desc": p_text
    }

with open('p:/BACKUP/URNA/Curso Roadmaps/aulas/desc_output.json', 'w', encoding='utf-8') as out:
    json.dump(data, out, indent=2, ensure_ascii=False)
