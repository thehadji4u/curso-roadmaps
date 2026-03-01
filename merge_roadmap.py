import re

def fix_roadmap():
    with open('roadmaps_new ERRADo.html', 'r', encoding='utf-8') as f:
        bad_html = f.read()
    
    with open('roadmaps_new.html', 'r', encoding='utf-8') as f:
        good_html = f.read()

    # Find all items that have a hyperlink in the bad HTML
    # We look for <a href="([^"]+)" class="item[^"]*">.*?<div class="item-title">\s*([^<]+?)\s*</div>.*?</a>
    # Actually the title might have a badge inside it.
    
    # We can find all blocks <a href="..." class="item..."> ... </a> in the bad HTML
    a_tag_blocks = re.findall(r'(<a href="([^"]+)" class="item[^"]*">.*?<div class="item-title">\s*([^<]+?)\s*(?:<span[^>]*>.*?</span>)?\s*</div>.*?</a>)', bad_html, re.DOTALL)
    
    for block_html, href, title_text in a_tag_blocks:
        title_clean = title_text.strip()
        print(f"Porting block for: '{title_clean}' to href: {href}")
        
        # In good HTML, the item might look like:
        # <div class="item">
        #   <div class="item-title">Title</div>
        #   <div class="item-desc">Desc</div>
        # </div>
        
        # We need to replace the ENTIRE <div class="item">...</div> with the block_html from the bad html
        # Regex to find the <div class="item"> block that contains <div class="item-title">title_clean</div>
        # Since the structure is quite simple:
        
        # We find <div class="item"> followed by any chars non-greedy until <div class="item-title">TITLE</div>
        # followed by any chars non-greedy until </div></div> (because it has item-title and item-desc)
        pattern = r'<div class="item(?:\s+highlight)?">\s*<div class="item-title">\s*' + re.escape(title_clean) + r'\s*</div>\s*<div class="item-desc">.*?</div>\s*</div>'
        
        good_html, count = re.subn(pattern, block_html.replace('\\', '\\\\'), good_html, flags=re.DOTALL)
        if count == 0:
            print(f"WARNING: Could not port block for {title_clean}, trying loose match.")
            pattern_loose = r'<div class="item(?:\s+highlight)?">\s*<div class="item-title">\s*' + re.escape(title_clean).replace('\\ ', r'\s+') + r'\s*</div>\s*<div class="item-desc">.*?</div>\s*</div>'
            good_html, count = re.subn(pattern_loose, block_html.replace('\\', '\\\\'), good_html, flags=re.DOTALL)
            if count == 0:
                print(f"  -> FAILED ALSO")
            else:
                print(f"  -> FIXED with loose match!")

    # Fix CSS classes that were inside <style>
    good_html = good_html.replace('family=Syne:wght@400;700;800&', 'family=Inter:wght@400;500;700;800&')
    good_html = good_html.replace("font-family: 'Syne', sans-serif;", "font-family: 'Inter', sans-serif;")
    
    # Also add the badge CSS to the good html if it is missing
    if "lesson-badge" not in good_html[:good_html.find('</style>')]:
        badge_style = """
    /* ─── LESSON LINK STYLES ──────────────────────────── */
    a.item {
      text-decoration: none;
      color: inherit;
      display: block;
    }
    a.item:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }
    .lesson-badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 9px;
      padding: 2px 7px;
      border-radius: 4px;
      margin-left: 7px;
      letter-spacing: 0.08em;
      vertical-align: middle;
      transition: all 0.2s;
      font-weight: 700;
    }
    .badge-github { background: rgba(88, 166, 255, 0.15); border: 1px solid rgba(88, 166, 255, 0.35); color: #79c0ff; }
    .badge-python { background: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.35); color: #93c5fd; }
    .badge-html { background: rgba(239, 68, 68, 0.15); border: 1px solid rgba(239, 68, 68, 0.35); color: #fca5a5; }
    .badge-js { background: rgba(245, 158, 11, 0.15); border: 1px solid rgba(245, 158, 11, 0.35); color: #fcd34d; }
    .badge-docker { background: rgba(6, 182, 212, 0.15); border: 1px solid rgba(6, 182, 212, 0.35); color: #67e8f9; }
    .badge-n8n { background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.35); color: #6ee7b7; }
"""
        good_html = good_html.replace('</style>', badge_style + '\n  </style>')

    with open('roadmaps_new.html', 'w', encoding='utf-8') as f:
        f.write(good_html)
    
    print("Done. Check roadmaps_new.html")

if __name__ == "__main__":
    fix_roadmap()
