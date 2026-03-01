import glob
import re

css_to_inject = """
    /* NEXT CARD STANDARDIZATION */
    .next-card { display: flex; align-items: center; justify-content: space-between; padding: 22px 24px; background: var(--surface); border: 1px solid var(--accent-border); border-radius: 10px; text-decoration: none; transition: all 0.2s; margin-top: 24px; }
    .next-card:hover { background: var(--accent-dim); }
    .next-card-label { font-family: 'JetBrains Mono', monospace; font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--accent); margin-bottom: 4px; font-weight: 600; }
    .next-card-title { font-family: 'Syne', sans-serif; font-size: 1.1rem; font-weight: 700; color: #fff; }
    .next-arrow { font-size: 1.5rem; color: var(--accent); }
"""

# Wait, let's verify if the original old CSS had JetBrains Mono for the label.
# In gh-02-branches-merge.html it was: .next-card-label { font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--accent); margin-bottom: 4px; }
# Inheriting body font usually for small uppercase labels is JetBrains Mono. Yes.

count = 0
for f in glob.glob('p:/BACKUP/URNA/Curso Roadmaps/aulas/*.html'):
    try:
        content = open(f, encoding='utf-8').read()
        
        # We only want to inject if it's not already there
        if "/* NEXT CARD STANDARDIZATION */" in content:
            continue
            
        # Replace the closing </style> tag with our injected CSS + </style>
        new_content = content.replace('</style>', css_to_inject + '</style>')
        
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as out:
                out.write(new_content)
            count += 1
            print(f"Injected CSS into {f}")
    except Exception as e:
        print(f"Error: {e}")

print(f"Files updated with CSS: {count}")
