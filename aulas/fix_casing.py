import glob
import re

count = 0
for f in glob.glob('p:/BACKUP/URNA/Curso Roadmaps/aulas/*.html'):
    try:
        content = open(f, encoding='utf-8').read()
        
        # Replace 'Próxima Aula →' with 'Próxima aula →'
        new_content, n = re.subn(r'>Próxima Aula →</a>', '>Próxima aula →</a>', content)
        
        if n > 0 and new_content != content:
            with open(f, 'w', encoding='utf-8') as out:
                out.write(new_content)
            count += 1
            print(f"Standardized button casing in: {f}")
    except Exception as e:
        print(f"Error: {e}")

print(f"Total files updated: {count}")
