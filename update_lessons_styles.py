import os
import re
import glob

TEMPLATE_PATH = "lesson-template-ATUALIZADO.html"
AULAS_DIR = "aulas"

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def extract_template_blocks(html):
    style_match = re.search(r'(<style>.*?</style>)', html, re.DOTALL)
    
    script_start = html.rfind('<script>')
    body_end = html.find('</body>', script_start)
    script_block = html[script_start:body_end].strip()
    
    return style_match.group(1), script_block

def migrate_lesson(filepath, tpl_style, tpl_script):
    content = read_file(filepath)
    
    # Extract current colors
    accent_match = re.search(r'--accent:\s*(.*?);', content)
    accent_dim_match = re.search(r'--accent-dim:\s*(.*?);', content)
    accent_border_match = re.search(r'--accent-border:\s*(.*?);', content)
    
    if not accent_match:
        print(f"[{filepath}] --accent not found. Skipping.")
        return
        
    accent = accent_match.group(1).strip()
    accent_dim = accent_dim_match.group(1).strip() if accent_dim_match else "rgba(255, 255, 255, 0.15)"
    accent_border = accent_border_match.group(1).strip() if accent_border_match else "rgba(255, 255, 255, 0.3)"
    
    # Process style block
    new_style = tpl_style.replace("{{ACCENT_COLOR}}", accent)
    new_style = new_style.replace("{{ACCENT_DIM}}", accent_dim)
    new_style = new_style.replace("{{ACCENT_BORDER}}", accent_border)
    new_style = new_style.replace("{{PROGRESSO_PERCENT}}", "0")
    
    # Process script block
    new_script = tpl_script.replace("{{ACCENT_COLOR}}", accent)
    new_script = new_script.replace("{{ACCENT_BORDER}}", accent_border)
    
    # Replace style
    content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)
    
    # Replace script
    script_start = content.rfind('<script>')
    body_end = content.find('</body>', script_start)
    if script_start != -1 and body_end != -1:
        content = content[:script_start] + new_script + '\n\n' + content[body_end:]
    
    # Replace progress bar structure
    pbw_pattern = r'<div class="(?:progress-bar-wrap|pbw)">(?:.|\n)*?</div>\s*</div>'
    pb_replacement = '<div class="progress-bar-wrap">\n    <div class="progress-bar-fill"></div>\n  </div>'
    content = re.sub(pbw_pattern, pb_replacement, content, count=1, flags=re.DOTALL)
    
    write_file(filepath, content)
    print(f"[{filepath}] Updated successfully. Accent: {accent}")

def main():
    if not os.path.exists(TEMPLATE_PATH):
        print(f"Template {TEMPLATE_PATH} not found.")
        return
        
    template_content = read_file(TEMPLATE_PATH)
    tpl_style, tpl_script = extract_template_blocks(template_content)
    
    html_files = glob.glob(os.path.join(AULAS_DIR, "*.html"))
    for file in html_files:
        migrate_lesson(file, tpl_style, tpl_script)

if __name__ == "__main__":
    main()
