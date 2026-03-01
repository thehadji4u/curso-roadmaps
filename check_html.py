import re
from pathlib import Path

path = Path('roadmaps_new.html')
content = path.read_text(encoding='utf-8')

# The structure of an item:
# <a href="..." class="item ...">
#   <div class="item-title">...</div>
#   <div class="item-desc">...</div>
# </a>   <-- This might end up as </div> by mistake!

# To find where an <a> tag is closed with </div>, we can look for:
# <a [^>]*class="item[^"]*"[^>]*>\s*<div class="item-title">.*?</div>\s*<div class="item-desc">.*?</div>\s*</div>

pattern = re.compile(
    r'(<a[^>]*class="item[^>]*>)'             # 1: group with the <a> opening tag
    r'(\s*<div class="item-title">.*?</div>)' # 2: title div
    r'(\s*<div class="item-desc">.*?</div>)'  # 3: desc div
    r'(\s*)(</div>)',                         # 4: whitespace, 5: wrong closing div
    flags=re.DOTALL
)

matches = pattern.findall(content)
print(f"Found {len(matches)} occurrences of <a> item closed with </div>.")

new_content = pattern.sub(
    lambda m: f"{m.group(1)}{m.group(2)}{m.group(3)}{m.group(4)}</a>",
    content
)

if len(matches) > 0:
    path.write_text(new_content, encoding='utf-8')
    print("Fixed them and wrote to file!")
else:
    print("No obvious </a> mismatch found. Looking deeper...")
    # Maybe the anchor wraps the badges but misses a closing quote?
    # Let's check for any <a href="...> without closing double quotes.
    bad_hrefs = re.findall(r'<a[^>]*href="[^"]*>[^<]*', content)
    print("Mismatched double quotes in href?:", [b for b in bad_hrefs if '"' not in b[b.index('href="')+6:]])

