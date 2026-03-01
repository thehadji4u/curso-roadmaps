import sys
with open('roadmaps_new.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    line_upper = line.upper()
    if 'ROADMAP-' in line_upper or '<!-- GITHUB' in line_upper or '<!-- OPENCLAW' in line_upper:
        if i > 800:
            print(f'Line {i+1}: {line.strip()}')
