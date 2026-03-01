import glob
import re
import json

data = {}
files = glob.glob('p:/BACKUP/URNA/Curso Roadmaps/aulas/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to match the whole section
    # Usually starts with <div class="section-label">// próximos passos</div> or similar
    # we can use a regex to capture everything from "<!-- PRÓXIMOS PASSOS -->" until the next "</div>" that closes the section, or until the end of the file.
    # Alternatively, just look for the div containing "next-card-title"
    match = re.search(r'(<div class="section-label">[^<]*</div>\s*<h2>.*?</h2>\s*<p.*?>.*?</p>\s*<a[^>]*next-card(?:-link)?[^>]*>.*?</a>)', content, re.DOTALL | re.IGNORECASE)
    
    if match:
        data[f] = {"matched": match.group(1)}
    else:
        # try another pattern
        match2 = re.search(r'(<div class="section-label">[^<]*</div>\s*<h2>.*?</h2>\s*<p.*?>.*?</p>\s*<a .*?</a>)', content, re.DOTALL)
        if match2:
            data[f] = {"matched": match2.group(1)}
        else:
            data[f] = {"matched": None}

with open('p:/BACKUP/URNA/Curso Roadmaps/aulas/footers.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent=2, ensure_ascii=False)
