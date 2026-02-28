import glob
import os

files = glob.glob('aulas/gh*.html') + glob.glob('aulas/html-01*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('class="pitfall"', 'class="callout callout-warn"')
    content = content.replace('class="pitfall-title"', 'class="callout-title"')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Updated pitfalls in early lessons.')
