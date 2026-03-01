import glob
import re
import os

HTML_FILES = glob.glob('p:/BACKUP/URNA/Curso Roadmaps/aulas/*.html')

new_footer_template = '''      <div class="next-card">
        <div class="next-card-info">
          <div class="next-label">{label}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>
        <a href="{href}" class="next-btn">Próxima Aula →</a>
      </div>'''

updated = 0
for file in HTML_FILES:
    content = open(file, encoding='utf-8').read()
    
    # We will look for <a href="..." class="next-card"> ... </a>
    # Let's write a very permissive regex just in case there are nested tags we are missing
    pattern = r'<a href="([^"]+)" class="next-card">\s*<div>\s*<div class="next-card-label">(.*?)</div>\s*<div class="next-card-title">(.*?)</div>(.*?)\s*</div>\s*(?:<div class="next-arrow">→</div>|<span class="next-arrow">→</span>)\s*</a>'
    
    def repl(m):
        href = m.group(1).strip()
        label = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        title = re.sub(r'<[^>]+>', '', m.group(3)).strip()
        
        # The description might be wrapped in another div, or just text
        raw_desc = m.group(4)
        desc = re.sub(r'<[^>]+>', '', raw_desc).strip() if raw_desc else ""
        
        return new_footer_template.format(href=href, label=label, title=title, desc=desc)

    new_content, count = re.subn(pattern, repl, content, flags=re.DOTALL)
    
    if count > 0 and new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file)} with {count} changes.")
        updated += 1
print(f"Total updated: {updated}")
