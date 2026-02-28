import glob
import os

files = glob.glob('aulas/*.html') + ['lesson-template.html']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The exact string may vary by spaces, but let's try direct replace first
    target1 = '<div style="display:flex;align-items:center;gap:10px;">'
    target2 = '<div style="display: flex; align-items: center; gap: 10px;">'
    
    if target1 in content or target2 in content:
        content = content.replace(target1, '<div class="nav-center">')
        content = content.replace(target2, '<div class="nav-center">')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")
        
print("Done.")
