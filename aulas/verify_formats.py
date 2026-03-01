import glob
import re

new_format_count = 0
old_format_count = 0

for f in glob.glob('p:/BACKUP/URNA/Curso Roadmaps/aulas/*.html'):
    try:
        content = open(f, encoding='utf-8').read()
        
        # New format uses <div class="next-card">
        if re.search(r'<div[^>]*class="[^"]*next-card[^"]*"', content):
            new_format_count += 1
        # Old format uses <a href="..." class="next-card">
        elif re.search(r'<a[^>]*class="[^"]*next-card[^"]*"', content):
            old_format_count += 1
            print(f"Old format found in: {f}")
    except Exception as e:
        print(f"Error reading {f}: {e}")

print(f"Total files with new format: {new_format_count}")
print(f"Total files with old format: {old_format_count}")
