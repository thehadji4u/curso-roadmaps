import glob
import re

for file in glob.glob("aulas/*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix inline analogy-real and analogy-tech
    new_content = re.sub(
        r'(\s*)<span class="analogy-real">(.*?)</span>\s*<span class="analogy-tech">→\s*(.*?)</span>',
        r'\1<span class="analogy-real">\2</span>\n\1<span class="analogy-arrow">→</span>\n\1<span class="analogy-tech">\3</span>',
        content
    )
    
    # Fix standalone analogy-tech with arrows inside
    new_content = re.sub(
        r'(\s*)<span class="analogy-tech">→\s*(.*?)</span>',
        r'\1<span class="analogy-arrow">→</span>\n\1<span class="analogy-tech">\2</span>',
        new_content
    )

    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed {file}")

print("Done")
