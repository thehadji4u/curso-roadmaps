import glob
import re

count = 0
for f in glob.glob('p:/BACKUP/URNA/Curso Roadmaps/aulas/*.html'):
    try:
        content = open(f, encoding='utf-8').read()
        # Find if it still has <a class="next-card"> instead of <div class="next-card">
        # In the new style, "next-card" is a div, and the 'a' tag has class "next-btn"
        if re.search(r'<a[^>]*class="[^"]*next-card[^"]*"', content):
            count += 1
            print(f)
    except Exception as e:
        print(e)
print(f"Total old format count: {count}")
