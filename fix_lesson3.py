import re
import os

path = r'aulas\html-01-semantico-estrutura.html'
print(f"Limpando as tags <style> manuais de {path}...")

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Remover todos os blocos <style> atuais
text = re.sub(r'<style>.*?</style>', '', text, flags=re.DOTALL)

# Inserir o link para lesson.css que o inject_styles.py espera
text = text.replace('</head>', '  <link rel="stylesheet" href="../assets/css/lesson.css">\n</head>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Arquivo preparado. Agora rode inject_styles.py e purge_css.py.")
