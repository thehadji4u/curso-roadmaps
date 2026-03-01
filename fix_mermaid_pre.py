import glob
import re

files = glob.glob('aulas/*.html')
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace <div class="mermaid"> with <pre class="mermaid">
    # and its corresponding </div> with </pre>.
    
    # First, let's fix the specific broken syntax in py-04 and html-03 by adding newlines
    content = re.sub(r'ContaBancaria <\|-- ContaCorrente : herança ContaBancaria <\|-- ContaPoupanca : herança',
                     'ContaBancaria <|-- ContaCorrente : herança\n          ContaBancaria <|-- ContaPoupanca : herança', content)
                     
    content = re.sub(r'B -->\|< 768px\| C\[📱 Mobile\] B -->\|768px - 1023px\| D\[📟 Tablet\]',
                     'B -->|< 768px| C[📱 Mobile]\n          B -->|768px - 1023px| D[📟 Tablet]', content)
    
    # Agora substituir div.mermaid por pre.mermaid
    # O regex precisa achar <div class="mermaid"> (com qualquer variação de espaço ou outras classes)
    # e substituir apenas a tag de abertura e a DE FECHAMENTO correspondente.
    pattern = r'(<div[^>]*class="mermaid"[^>]*>)(.*?)(</div>)'
    
    matches = re.findall(pattern, content, flags=re.DOTALL)
    
    if matches:
        new_content = re.sub(pattern, lambda m: f'<pre class="mermaid">{m.group(2)}</pre>', content, flags=re.DOTALL)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {len(matches)} mermaid blocks in {fpath}")
        
    else:
        # Check if already pre.mermaid
        pre_matches = re.findall(r'<pre[^>]*class="mermaid"[^>]*>', content)
        if pre_matches:
            print(f"File {fpath} already using <pre> tags.")
        else:
            print(f"File {fpath} has no mermaid blocks.")

