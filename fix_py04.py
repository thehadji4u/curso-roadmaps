import re
import os

path = 'aulas/py-04-poo.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace HEAD entirely
new_head = """<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aula 08 — POO na Prática | 🐍 Python</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
  <style>
    /* ─── TOKENS ────────────────────────────────────────────── */
    :root {
      --bg: #0a0a0f;
      --surface: #111118;
      --surface2: #16161f;
      --border: #1e1e2e;
      --text: #e8e8f0;
      --muted: #8585a8;

      --accent: #3b82f6;       /* ex: #3b82f6 para Python */
      --accent-dim: rgba(59, 130, 246, 0.12);     /* ex: rgba(59,130,246,0.15) */
      --accent-border: rgba(59, 130, 246, 0.35); /* ex: rgba(59,130,246,0.3) */

      /* Semantic colors */
      --success: #10b981;
      --warn: #f59e0b;
      --danger: #ef4444;
      --info: #06b6d4;
    }
  </style>
  <link rel="stylesheet" href="../assets/css/lesson.css">
</head>"""

content = re.sub(r'<head>.*?</head>', new_head, content, flags=re.DOTALL)

# 2. Section -> div class="section"
content = content.replace('<section>', '<div class="section">')
content = content.replace('</section>', '</div>')

# 3. main -> div class="page"
content = content.replace('<main>', '<div class="page">')
content = content.replace('</main>', '</div><!-- /page -->')

# 4. Remove id="progressBar"
content = content.replace('id="progressBar"', '')

# 5. Replace bottom script entirely
new_script = """<script>
    // Initialize syntax highlighting
    document.addEventListener('DOMContentLoaded', () => {
      hljs.highlightAll();
    });

    // Initialize Mermaid
    mermaid.initialize({
      startOnLoad: true,
      theme: 'dark',
      themeVariables: {
        primaryColor: '#3b82f6',
        primaryTextColor: '#e8e8f0',
        primaryBorderColor: 'rgba(59, 130, 246, 0.35)',
        lineColor: '#8585a8',
        background: '#111118',
        mainBkg: '#16161f',
        nodeBorder: '#3b82f6'
      }
    });

    // Scroll progress indicator (update progress bar)
    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = (scrollTop / docHeight) * 100;
      document.querySelector('.progress-bar-fill').style.width = progress + '%';
    });
  </script>"""

content = re.sub(r'<script>.*?</script>', new_script, content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"refactored {path}")
