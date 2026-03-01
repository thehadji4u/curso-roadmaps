import re
from pathlib import Path
from html.parser import HTMLParser

class RoadmapFixer(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.output = []
        
    def handle_starttag(self, tag, attrs):
        # When we start a tag, we record it
        d_attrs = dict(attrs)
        self.tags.append(tag)
        
        # Build the original tag string to output
        attr_str = " ".join([f'{k}="{v}"' if v is not None else k for k,v in attrs])
        self.output.append(f"<{tag} {attr_str}>" if attr_str else f"<{tag}>")

    def handle_endtag(self, tag):
        # We expect this end tag to match the last start tag
        if self.tags:
            last_tag = self.tags.pop()
            if last_tag != tag:
                # Mismatch! 
                # Is it an item block where user opened <a> but closed </div>?
                if last_tag == 'a' and tag == 'div':
                    # Fix it: close 'a' instead of 'div'
                    self.output.append(f"</a>")
                    print("Fixed mismatch: expected </a> but got </div>")
                    return
                # Is it an item block where my regex opened <div class="item"> and closed </a>?
                elif last_tag == 'div' and tag == 'a':
                    self.output.append(f"</div>")
                    print("Fixed mismatch: expected </div> but got </a>")
                    return
                else:
                    # Generic mismatch logic - let's forcefully close the last tag 
                    # assuming the layout logic was slightly flawed.
                    self.output.append(f"</{last_tag}>")
            else:
                self.output.append(f"</{tag}>")
        else:
             self.output.append(f"</{tag}>")

    def handle_data(self, data):
        self.output.append(data)

    def handle_comment(self, data):
        self.output.append(f"<!--{data}-->")

    def handle_entityref(self, name):
        self.output.append(f"&{name};")

    def handle_charref(self, name):
        self.output.append(f"&#{name};")

    def handle_decl(self, decl):
        self.output.append(f"<!{decl}>")

    # Some tags are self-closing like <img>, <meta>, <link>, <svg>, <path>, <rect>...
    def handle_startendtag(self, tag, attrs):
        attr_str = " ".join([f'{k}="{v}"' if v is not None else k for k,v in attrs])
        self.output.append(f"<{tag} {attr_str}/>" if attr_str else f"<{tag}/>")

# Let's write a simpler, foolproof line-oriented approach based on the exact file structure.
# The `items-grid` structure is strictly:
# <div class="items-grid">
#   <div class="item"> or <a href="..." class="item ...">
#      <div class="item-title">...</div>
#      <div class="item-desc">...</div>
#   </div> or </a>
# </div>

path = Path('roadmaps_new.html')
content = path.read_text(encoding='utf-8')

lines = content.split('\n')
new_lines = []
expecting_close = None # Either 'div' or 'a'

for i, line in enumerate(lines):
    stripped = line.strip()
    
    # Check if this line is an item opening
    if stripped.startswith('<div class="item"'):
        expecting_close = 'div'
        new_lines.append(line)
    elif stripped.startswith('<a href=') and 'class="item' in stripped:
        expecting_close = 'a'
        new_lines.append(line)
    # Check if this line is supposed to be the item closing
    elif expecting_close and (stripped == '</div>' or stripped == '</a>'):
        # Just use indentation to guess it's the wrapper close
        if line.startswith('              <'):
            # The inner <div item-title> and item-desc are indented differently,
            # wait, let's just close whatever was expected!
            # Wait, item-title and item-desc also have </div>.
            pass
        
        # A safer check: look locally.
        new_lines.append(line)
    else:
        new_lines.append(line)


# Actually, my previous regex ruined 12 occurrences of </div> at the end of the items.
# Let's fix ALL items iteratively using regex!

# A valid item matches:
# (<div class="item"> OR <a href="..." class="item...">)
# \s*<div class="item-title">.*?</div>
# \s*<div class="item-desc">.*?</div>
# \s*(</div> OR </a>)

# Let's repair EVERY item block in the whole file:
def repair_item_block(match):
    opening_tag = match.group(1)   # e.g. <div class="item"> or <a href="...">
    inner_content = match.group(2) # title and desc and whitespace
    closing_tag = match.group(3)   # </div> or </a>
    
    # The correct closing tag depends on the opening tag
    if opening_tag.startswith('<a '):
        correct_closing = '</a>'
    else:
        correct_closing = '</div>'
    
    return f"{opening_tag}{inner_content}{correct_closing}"

# Match an item container opening, its children, and the immediate closing tag.
# Using greedy match for inner content might be dangerous, but if we assume
# inner content is just 2 divs, we can be exact.

item_pattern = re.compile(
    r'(<a\s+href="[^"]*"\s+class="item[^>]*>|<div\s+class="item">)' # 1: opening
    r'(\s*<div\s+class="item-title">.*?</div>\s*<div\s+class="item-desc">.*?</div>\s*)' # 2: inner childs
    r'(</div>|</a>)', # 3: closing
    flags=re.DOTALL
)

repaired_content = item_pattern.sub(repair_item_block, content)
path.write_text(repaired_content, encoding='utf-8')
print("Repaired all item blocks successfully!")
