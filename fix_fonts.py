import os
import glob
import re

HLJS_LINK = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">'

def fix_template():
    tpl_path = "lesson-template-ATUALIZADO.html"
    with open(tpl_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix body font
    content = re.sub(
        r"body\s*\{[^}]*font-family:\s*'JetBrains Mono',\s*monospace;",
        "body {\n      background: var(--bg);\n      color: var(--text);\n      font-family: 'Syne', sans-serif;\n      line-height: 1.7;\n      overflow-x: hidden;",
        content
    )
    with open(tpl_path, "w", encoding="utf-8") as f:
        f.write(content)

def fix_lessons():
    html_files = glob.glob(os.path.join("aulas", "*.html"))
    for filepath in html_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 1. Fix body font inside the <style> block
        content = re.sub(
            r"body\s*\{[^}]*font-family:\s*'JetBrains Mono',\s*monospace;",
            "body {\n      background: var(--bg);\n      color: var(--text);\n      font-family: 'Syne', sans-serif;\n      line-height: 1.7;\n      overflow-x: hidden;",
            content
        )

        # 2. Inject github-dark css link if missing
        if "github-dark.min.css" not in content and "HLJS github-dark inline" not in content:
            # We insert it right before the highlight.js script
            script_tag = '<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>'
            if script_tag in content:
                content = content.replace(script_tag, HLJS_LINK + '\n  ' + script_tag)

        # 3. Double check pitfalls were replaced in case any missed
        content = content.replace('class="pitfall"', 'class="callout callout-warn"')
        content = content.replace('class="pitfall-title"', 'class="callout-title"')

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed fonts/hljs link in {filepath}")

fix_template()
fix_lessons()
