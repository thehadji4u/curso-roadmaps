import glob
import re
import os

HTML_FILES = glob.glob('p:/BACKUP/URNA/Curso Roadmaps/aulas/*.html')

count_files = 0
for file in HTML_FILES:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Match the current standardized div.next-card block
    pattern_card = re.compile(
        r'<div class="next-card">\s*'
        r'<div class="next-card-info">\s*'
        r'<div class="next-label">(.*?)</div>\s*'
        r'<h\d>(.*?)</h\d>'
        r'(?:\s*<p>.*?</p>)?\s*'
        r'</div>\s*'
        r'<a href="([^"]+)" class="next-btn">.*?</a>\s*'
        r'</div>',
        re.DOTALL
    )
    
    def repl_card(m):
        label = m.group(1).strip()
        # Ensure we use 'Próxima Aula' as in the user's snippet, replacing 'PRÓXIMA AULA'
        label = label.replace('PRÓXIMA AULA', 'Próxima Aula')
        title = m.group(2).strip()
        href = m.group(3).strip()
        
        return f'''<a href="{href}" class="next-card">
        <div>
          <div class="next-card-label">{label}</div>
          <div class="next-card-title">{title}</div>
        </div>
        <div class="next-arrow">→</div>
      </a>'''

    new_content, n1 = pattern_card.subn(repl_card, content)
    
    # Also standardize the section label before "O que vem a seguir" to // próxima aula
    pattern_section = re.compile(
        r'<div class="section-label">\s*//\s*([^<]+)\s*</div>\s*(<h2(?:[^>]*)>O que vem a seguir\?</h2>)',
        re.IGNORECASE
    )
    
    new_content, n2 = pattern_section.subn(r'<div class="section-label">// próxima aula</div>\n      \2', new_content)

    if n1 > 0 or n2 > 0:
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count_files += 1
            print(f"Updated {os.path.basename(file)} (Card: {n1}, Section: {n2})")

print(f"Total updated files: {count_files}")
