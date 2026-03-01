import re

with open('roadmaps_new ERRADo.html', 'r', encoding='utf-8') as f:
    text = f.read()

badges = re.findall(r'<span class="lesson-badge[^"]*">([^<]+)</span>', text)
for i, b in enumerate(badges):
    print(b)
