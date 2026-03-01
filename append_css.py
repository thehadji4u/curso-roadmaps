import os

css_path = r'assets\css\lesson.css'
new_css = """

/* ─── COMPONENTES ADICIONAIS (AULA 03) ──────────────────── */
.html-tag { display: inline-block; background: rgba(239,68,68,0.12); border: 1px solid rgba(239,68,68,0.3); color: #f87171; padding: 2px 8px; border-radius: 4px; font-family: 'JetBrains Mono', monospace; font-size: 13px; }

/* ── Compare split ── */
.compare-split { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0; }
@media (max-width: 600px) { .compare-split { grid-template-columns: 1fr; } }
.compare-old { background: rgba(239,68,68,0.05); border: 1px solid rgba(239,68,68,0.2); border-radius: 8px; padding: 16px; }
.compare-new { background: rgba(16,185,129,0.05); border: 1px solid rgba(16,185,129,0.2); border-radius: 8px; padding: 16px; }
.compare-label { font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 10px; font-weight: 600; }
.compare-old .compare-label { color: #f87171; }
.compare-new .compare-label { color: #34d399; }

/* ── Pitfall ── */
.pitfall { background: rgba(239,68,68,0.06); border: 1px solid rgba(239,68,68,0.25); border-radius: 10px; padding: 20px; margin: 16px 0; }
.pitfall-title { color: #f87171; font-weight: 700; margin-bottom: 8px; }

/* ── Glossary ── */
.glossary-item { padding: 14px 0; border-bottom: 1px solid var(--border); }
.glossary-term { color: var(--accent); font-weight: 700; margin-bottom: 4px; }
.glossary-def { color: var(--muted); font-size: 13px; }

/* ── Next card ── */
.next-card { display: flex; align-items: center; justify-content: space-between; padding: 22px 24px; background: var(--surface); border: 1px solid var(--accent-border); border-radius: 10px; text-decoration: none; transition: all 0.2s; }
.next-card:hover { background: var(--accent-dim); }
.next-card-label { font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--accent); margin-bottom: 4px; }
.next-card-title { font-family: 'Syne', sans-serif; font-size: 1.1rem; font-weight: 700; color: #fff; }

/* ── DOM tree visual ── */
.dom-tree { background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 24px; font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 2; }
.dom-tree .node { color: #f87171; }
.dom-tree .attr { color: #79c0ff; }
.dom-tree .text { color: #a5d6ff; }
.dom-tree .comment { color: #8b949e; font-style: italic; }
.tree-indent-1 { padding-left: 20px; }
.tree-indent-2 { padding-left: 40px; }
.tree-indent-3 { padding-left: 60px; }
.tree-indent-4 { padding-left: 80px; }
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(new_css)

print("CSS components appended successfully.")
