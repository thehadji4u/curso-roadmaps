import os
import re
import glob

CSS_PATH = os.path.join("assets", "css", "lesson.css")
TEMPLATE_PATH = "lesson-template.html"
AULAS_DIR = "aulas"

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    # 1. Update CSS file
    css_content = read_file(CSS_PATH)
    
    # Check if we already added the import
    import_statement = "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@300;400;700&display=swap');\n\n"
    
    if "@import url" not in css_content:
        css_content = import_statement + css_content
        
    css_content = css_content.replace("'Syne'", "'Inter'")
    write_file(CSS_PATH, css_content)
    print(f"Updated CSS file: {CSS_PATH}")

    # 2. Update HTML files (template + aulas)
    files_to_process = [TEMPLATE_PATH] + glob.glob(os.path.join(AULAS_DIR, "*.html"))
    for filepath in files_to_process:
        content = read_file(filepath)
        
        # Remove the <link> tag for google fonts
        # Note: sometimes it has \n and spaces inside
        pattern = r'<link[^>]*?fonts\.googleapis\.com[^>]*?>\s*'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        write_file(filepath, content)
        print(f"Updated HTML file: {filepath}")

if __name__ == "__main__":
    main()
