import glob
import re
import os

files = glob.glob('aulas/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The duplicated block looks like:
    #   <style>
    #     /* ─── TOKENS ────────────────────────────────────────────── */
    #     :root {
    #       ...
    #     }
    #   </style>
    #   <link rel="stylesheet" href="../assets/css/lesson.css">
    
    # We will find all occurrences of this pattern.
    pattern = r'<style>\s*/\* ─── TOKENS ──.*?</style>\s*<link rel="stylesheet" href="\.\./assets/css/lesson\.css">'
    
    matches = re.findall(pattern, content, flags=re.DOTALL)
    
    if len(matches) > 1:
        print(f"File {filepath} has {len(matches)} token style blocks. Removing duplicates.")
        # Replace all but the first one
        # Split by the exact match and rejoin, keeping only the first one
        
        # Actually it's safer to just replace all occurrences with empty string, 
        # EXCEPT the first one.
        
        # Find first match index
        match_obj = re.search(pattern, content, flags=re.DOTALL)
        if match_obj:
            first_match_str = match_obj.group(0)
            
            # Remove all matches
            content = re.sub(pattern, "", content, flags=re.DOTALL)
            
            # Put the first match back right before </head>
            content = content.replace("</head>", f"{first_match_str}\n</head>")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {filepath}")
    else:
        # Check if there are other empty styles or weird duplicated tags
        # Sometimes there's a `<style>\n<style>` or `<style><!-- TOKENS`
        pass
        
print("Done.")
