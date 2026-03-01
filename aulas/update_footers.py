import glob
import re
import os

def update_footers():
    files = glob.glob('p:/BACKUP/URNA/Curso Roadmaps/aulas/*.html')
    
    # Let's map emojis and topics
    # gh-* -> 🐙 GitHub
    # html-* -> 🌐 HTML/CSS
    # py-* -> 🐍 Python
    # js-* -> ⚡ JavaScript (Wait, js-01 is "⚡ JavaScript")
    
    # We first parse to find exactly the HTML blocks to replace
    # We will use BeautifulSoup if available, but regex is safer to keep formatting.
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # 1. Replace section label
        # <div class="section-label">// próximos passos</div>
        # or <div class="section-label">// Próximos passos</div>
        content = re.sub(r'<div class="section-label">\s*//\s*próximos passos\s*</div>', '<div class="section-label">// PRÓXIMOS PASSOS</div>', content, flags=re.IGNORECASE)
        
        # 2. Extract next-card-label and fix it
        # We look for <div class="next-card-label">...</div> or <div class="next-label">...</div>
        # and <div class="next-card-title">...</div> or <div class="next-title">...</div>
        
        # We need to preserve the anchor tag and the overall structure, just update the label text to the format:
        # PRÓXIMA AULA • [Emoji] [Topic]
        
        # Since each file has a specific next lesson, we can derive the topic from the text that is currently there.
        # It usually contains the emoji and topic. e.g "Próxima aula · 🐙 GitHub" -> "PRÓXIMA AULA • 🐙 GitHub"
        # "Aula 10 → HTML/CSS" (missing globe emoji maybe?) -> "PRÓXIMA AULA • 🌐 HTML/CSS"
        
        def replace_label(match):
            old_label = match.group(2)
            # Find emoji and topic
            topic_str = ""
            if "GitHub" in old_label:
                topic_str = "🐙 GitHub"
            elif "HTML" in old_label or "CSS" in old_label:
                topic_str = "🌐 HTML/CSS"
            elif "Python" in old_label:
                topic_str = "🐍 Python"
            elif "JavaScript" in old_label or "JS" in old_label:
                topic_str = "⚡ JavaScript"
            
            # fallback
            if not topic_str:
                if "🐙" in old_label: topic_str = "🐙 GitHub"
                elif "🌐" in old_label: topic_str = "🌐 HTML/CSS"
                elif "🐍" in old_label: topic_str = "🐍 Python"
                elif "⚡" in old_label: topic_str = "⚡ JavaScript"
                
            if not topic_str:
                # If still nothing, just keep PRÓXIMA AULA
                return f'{match.group(1)}PRÓXIMA AULA{match.group(3)}'
                
            return f'{match.group(1)}PRÓXIMA AULA • {topic_str}{match.group(3)}'
            
        content = re.sub(r'(<div class="next-card-label">)(.*?)(</div>)', replace_label, content)
        content = re.sub(r'(<div class="next-label">)(.*?)(</div>)', replace_label, content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)

if __name__ == '__main__':
    update_footers()
    print("Done updating footers.")
