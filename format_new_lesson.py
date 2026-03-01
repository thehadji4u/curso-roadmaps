import re
import sys
import os

def format_lesson(filepath):
    if not os.path.exists(filepath):
        print(f"Erro: O arquivo '{filepath}' não foi encontrado.")
        sys.exit(1)

    print(f"Formatando {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Extrair cores de accent (se existirem no arquivo original)
    accent_match = re.search(r'--accent:\s*(.*?);', content)
    accent_dim_match = re.search(r'--accent-dim:\s*(.*?);', content)
    accent_border_match = re.search(r'--accent-border:\s*(.*?);', content)

    # Cores padrão caso não encontre (ex: Python)
    accent = accent_match.group(1).strip() if accent_match else "#3b82f6"
    accent_dim = accent_dim_match.group(1).strip() if accent_dim_match else "rgba(59, 130, 246, 0.12)"
    accent_border = accent_border_match.group(1).strip() if accent_border_match else "rgba(59, 130, 246, 0.35)"

    # Derivar a cor do node border para o Mermaid (sem opacidade)
    mermaid_node_border = accent
    mermaid_border_color = accent_border

    # 2. Padronizar o <head> (CSS, HLJS, Mermaid, Variáveis)
    # Primeiro vamos remover todas as tags <style>, link do lesson.css e scripts do HLJS/Mermaid
    content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<link[^>]*highlight[^>]*>', '', content)
    content = re.sub(r'<script[^>]*highlight\.min\.js[^>]*></script>', '', content)
    content = re.sub(r'<script[^>]*mermaid\.min\.js[^>]*></script>', '', content)
    content = re.sub(r'<link[^>]*lesson\.css[^>]*>', '', content)

    # Adicionar o bloco padronizado antes do </head>
    standard_head_content = f"""
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>

  <style>
    /* ─── TOKENS ────────────────────────────────────────────── */
    :root {{
      --bg: #0a0a0f;
      --surface: #111118;
      --surface2: #16161f;
      --border: #1e1e2e;
      --text: #e8e8f0;
      --muted: #8585a8;

      --accent: {accent};
      --accent-dim: {accent_dim};
      --accent-border: {accent_border};

      /* Semantic colors */
      --success: #10b981;
      --warn: #f59e0b;
      --danger: #ef4444;
      --info: #06b6d4;
    }}
  </style>
  <link rel="stylesheet" href="../assets/css/lesson.css">
"""

    # Extrair regras CSS exclusivas do arquivo original (ignorando os TOKENS padrão)
    # Isso garante que se a aula 10 tiver uma classe ".minha-tabela", ela não seja perdida
    style_blocks = re.findall(r'<style>(.*?)</style>', content, flags=re.DOTALL)
    custom_css = ""
    for block in style_blocks:
        # Remover o bloco root de tokens padrão que sempre descartamos
        block = re.sub(r':root\s*\{[^}]*\}', '', block, flags=re.DOTALL)
        # Limpar espaços
        block = block.strip()
        if block:
            custom_css += "\n" + block

    # Se houver CSS customizado que restou, vamos injetar DE VOLTA no HTML
    # (Poderíamos anexar no lesson.css, mas injetar no HTML da própria aula é mais seguro por agora)
    if custom_css.strip():
        standard_head_content = standard_head_content.replace(
            '</style>', 
            f'\n    /* ── CUSTOM CLASSES DA AULA ── */\n{custom_css}\n  </style>'
        )

    content = content.replace('</head>', standard_head_content + '</head>')

    # 3. Remover fontes inline do <body> (o lesson.css já cuida disso)
    content = re.sub(r'body\s*\{[^}]*font-family:[^}]*\}', '', content, flags=re.IGNORECASE)

    # 4. Substituir <main> por <div class="page">
    content = content.replace('<main>', '<div class="page">')
    content = content.replace('</main>', '</div><!-- /page -->')

    # 5. Substituir <section> por <div class="section">
    content = content.replace('<section>', '<div class="section">')
    content = content.replace('</section>', '</div>')

    # 6. Atualizar classes de Pitfall para o padrão de callouts modernos
    content = content.replace('class="pitfall"', 'class="callout callout-warn"')
    content = content.replace('class="pitfall-title"', 'class="callout-title"')

    # 7. Garantir a barra de progresso após a abertura do <body>
    pbw_pattern = r'<div class="(?:progress-bar-wrap|pbw)">(?:.|\n)*?</div>\s*</div>?'
    pb_replacement = '<div class="progress-bar-wrap">\n    <div class="progress-bar-fill"></div>\n  </div>'
    
    if not re.search(pbw_pattern, content):
        # Injetar logo após o body se não existir ainda
        content = content.replace('<body>', '<body>\n\n  ' + pb_replacement)
    else:
        # Substituir a existente
        content = re.sub(pbw_pattern, pb_replacement, content, count=1, flags=re.DOTALL)

    # 8. Atualizar o bloco de scripts no final (HLJS, Mermaid, Progresso)
    # Remover scripts antigos que inicializavam essas configs
    content = re.sub(r'<script>\s*(?:hljs|mermaid|document\.addEventListener|const\s+progress).*?</script>', '', content, flags=re.DOTALL)
    
    standard_script = f"""<script>
    // Initialize syntax highlighting
    document.addEventListener('DOMContentLoaded', () => {{
      hljs.highlightAll();
    }});

    // Initialize Mermaid
    mermaid.initialize({{
      startOnLoad: true,
      theme: 'dark',
      themeVariables: {{
        primaryColor: '{accent}',
        primaryTextColor: '#e8e8f0',
        primaryBorderColor: '{mermaid_border_color}',
        lineColor: '#8585a8',
        background: '#111118',
        mainBkg: '#16161f',
        nodeBorder: '{mermaid_node_border}'
      }}
    }});

    // Scroll progress indicator
    window.addEventListener('scroll', () => {{
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = (scrollTop / docHeight) * 100;
      const progressFill = document.querySelector('.progress-bar-fill');
      if (progressFill) progressFill.style.width = progress + '%';
    }});
  </script>"""
    content = content.replace('</body>', standard_script + '\n</body>')

    # 9. Trocar div.mermaid por pre.mermaid para proteger contra o Prettier do VSCode
    # E arrumar quebras de linha caso o HTML formater já tenha espremido
    def fix_mermaid(match):
        m_content = match.group(0)
        # Corrigir tags HTML quebrando a sintaxe
        m_content = m_content.replace('<br>\n', '<br>').replace('<br/>\n', '<br>')
        
        # Tentar descolapsar nós de grafos (ex: C[Mobile] B -->)
        m_content = re.sub(r'\]\s+([A-Z0-9_]+)\s*-->', r']\n          \1 -->', m_content)
        # Tentar descolapsar elementos de classe (ex: : herança ContaBancaria)
        m_content = re.sub(r':\s*herança\s+([A-Z][a-zA-Z0-9_]+)', r': herança\n          \1', m_content)
        
        # Substituir div por pre
        m_content = re.sub(r'^<div', '<pre', m_content)
        m_content = re.sub(r'</div>$', '</pre>', m_content)
        
        return m_content
    content = re.sub(r'<div class="mermaid">.*?</div>', fix_mermaid, content, flags=re.DOTALL)

    # 10. Limpar múltiplas linhas em branco que podem ter sobrado
    content = re.sub(r'\n{4,}', '\n\n', content)

    # Salvar alterações
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Sucesso! {filepath} agora segue o padrão oficial de estilos.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for file in sys.argv[1:]:
            format_lesson(file)
    else:
        print("Uso: python format_new_lesson.py <caminho_da_aula.html>")
        print("Exemplo: python format_new_lesson.py aulas/aula-11.html")
