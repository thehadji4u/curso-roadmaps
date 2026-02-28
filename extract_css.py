import os
import re
import glob

# Paths
TEMPLATE_PATH = "lesson-template.html"
CSS_OUT_DIR = os.path.join("assets", "css")
CSS_OUT_PATH = os.path.join(CSS_OUT_DIR, "lesson.css")
AULAS_DIR = "aulas"

# Ensure dir exists
os.makedirs(CSS_OUT_DIR, exist_ok=True)

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    template_content = read_file(TEMPLATE_PATH)
    
    # 1. Extract the CSS base from the template
    # Find start of standard rules
    base_start_idx = template_content.find("/* ─── RESET & BASE ──────────────────────────────────────── */")
    style_end_idx = template_content.find("</style>")
    
    if base_start_idx == -1 or style_end_idx == -1:
        print("Could not find CSS boundaries in template!")
        return
        
    extracted_css = template_content[base_start_idx:style_end_idx].strip()
    write_file(CSS_OUT_PATH, extracted_css)
    print(f"Created global CSS file: {CSS_OUT_PATH}")

    files_to_process = [TEMPLATE_PATH] + glob.glob(os.path.join(AULAS_DIR, "*.html"))
    
    for filepath in files_to_process:
        content = read_file(filepath)
        
        # We need to extract the tokens block or existing accent variables
        accent_match = re.search(r'--accent:\s*(.*?);', content)
        accent_dim_match = re.search(r'--accent-dim:\s*(.*?);', content)
        accent_border_match = re.search(r'--accent-border:\s*(.*?);', content)
        
        accent = accent_match.group(1).strip() if accent_match else "{{ACCENT_COLOR}}"
        accent_dim = accent_dim_match.group(1).strip() if accent_dim_match else "{{ACCENT_DIM}}"
        accent_border = accent_border_match.group(1).strip() if accent_border_match else "{{ACCENT_BORDER}}"
        
        # Calculate relative path to the CSS file
        if "aulas" in filepath:
            css_link_path = "../assets/css/lesson.css"
        else:
            css_link_path = "assets/css/lesson.css"

        new_style_block = f"""<style>
    /* ─── TOKENS ────────────────────────────────────────────── */
    :root {{
      --bg: #0a0a0f;
      --surface: #111118;
      --surface2: #16161f;
      --border: #1e1e2e;
      --text: #e8e8f0;
      --muted: #8585a8;

      --accent: {accent};       /* ex: #3b82f6 para Python */
      --accent-dim: {accent_dim};     /* ex: rgba(59,130,246,0.15) */
      --accent-border: {accent_border}; /* ex: rgba(59,130,246,0.3) */

      /* Semantic colors */
      --success: #10b981;
      --warn: #f59e0b;
      --danger: #ef4444;
      --info: #06b6d4;
    }}
  </style>
  <link rel="stylesheet" href="{css_link_path}">"""

        content = re.sub(r'<style>.*?</style>', new_style_block, content, flags=re.DOTALL)
        
        write_file(filepath, content)
        print(f"Updated: {filepath}")

if __name__ == "__main__":
    main()
