import glob
import re
import os

files = glob.glob('p:/BACKUP/URNA/Curso Roadmaps/aulas/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Let's find exactly the block:
    # <div class="section-label">// próximos passos</div>
    # <h2>...</h2>
    # <p>...</p>
    # <a href="..." class="next-card">
    #   <div>
    #     <div class="next-card-label">Próxima aula · 🐙 GitHub</div>
    #     <div class="next-card-title">Git — Branches, Merge & Conflitos</div>
    
    # Extract
    pattern = r'<div class="next-card-label">(.*?)</div>\s*<div class="next-card-title">(.*?)</div>'
    match = re.search(pattern, content)
    if match:
        label = match.group(1)
        title = match.group(2)
        print(f"File: {os.path.basename(f)}")
        print(f"  Old Label: {label}")
        print(f"  Title: {title}")
        
        # We need to change "Próxima aula · [algo]" to "PRÓXIMA AULA • [algo]" and remove any reference to "Aula 0X"
        # Wait, the label usually is "Próxima aula · 🐙 GitHub". We want "PRÓXIMA AULA • 🐙 GitHub"
        new_label = label.replace("Próxima aula ·", "PRÓXIMA AULA •").replace("Próxima aula", "PRÓXIMA AULA")
        
        # If there's an explicit Aula XX, we should remove it? Let's check first.
        print(f"  New Label: {new_label}")
    else:
        print(f"File: {os.path.basename(f)} NO MATCH")
