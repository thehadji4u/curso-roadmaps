# 📋 Índice de Aulas — Fonte da Verdade

> **50 aulas densas (~30 min cada), ordenadas por prioridade de geração.**
> Cada aula agrupa cards relacionados do roadmap em uma única experiência coesa.
> Atualize o status conforme as aulas forem sendo criadas.

## Legenda
- `[ ]` Não iniciada · `[~]` Em progresso · `[x]` Concluída

## Estrutura do ID
```
{PRIORIDADE:02}-{SIGLA}-{SEQUENCIA:02}
```
- Prioridade define a ordem de geração (01 = criar primeiro)
- Exemplo: `01-GH-01`, `05-PY-02`, `37-AI-01`

## Arquivo de saída
Todos os HTMLs ficam em `outputs/aulas/` com o nome exato da coluna **Arquivo**.

---

## 🟥 PRIORIDADE 1 — BASE UNIVERSAL
> Fundamentos que desbloqueiam tudo. Sem isso, nada avança.
> Referência: Semanas 1–4 do roadmap.

| ID | Status | Trilha | Título da Aula | Cards agrupados | Arquivo |
|---|---|---|---|---|---|
| `01-GH-01` | `[x]` | 🐙 GitHub | Git — Do zero ao primeiro commit | O que é controle de versão · Instalação & configuração · Repositório local · Commit · Diff & inspeção | `gh-01-primeiro-commit.html` |
| `02-GH-02` | `[x]` | 🐙 GitHub | Git — Branches, Merge & Conflitos | Branches · Merge · Desfazendo mudanças · Stash | `gh-02-branches-merge.html` |
| `03-HTML-01` | `[x]` | 🌐 HTML/CSS | HTML Semântico & Estrutura | Semântica · Formulários · Media & embeds | `html-01-semantico-estrutura.html` |
| `04-HTML-02` | `[x]` | 🌐 HTML/CSS | CSS — Box Model, Flexbox & Grid | Box Model · Flexbox · CSS Grid · Cascade & Specificity | `html-02-box-flexbox-grid.html` |
| `05-PY-01` | `[x]` | 🐍 Python | Python — Ambiente & Primeiros Passos | Instalação & ambiente · Tipos & variáveis · Strings & formatação | `py-01-ambiente-primeiros-passos.html` |
| `06-PY-02` | `[x]` | 🐍 Python | Python — Lógica & Funções | Estruturas de controle · Funções · List comprehensions | `py-02-logica-funcoes.html` |

---

## 🟧 PRIORIDADE 2 — FUNDAMENTOS SÓLIDOS
> Completam a base e introduzem boas práticas.
> Referência: Semanas 5–8 do roadmap.

| ID | Status | Trilha | Título da Aula | Cards agrupados | Arquivo |
|---|---|---|---|---|---|
| `07-PY-03` | `[x]` | 🐍 Python | Python — Estruturas de Dados | Coleções · Arquivos · Tratamento de erros | `py-03-estruturas-dados.html` |
| `08-PY-04` | `[x]` | 🐍 Python | Python — Orientação a Objetos | POO · Módulos & pacotes · Decorators & closures | `py-04-orientacao-objetos.html` |
| `09-HTML-03` | `[x]` | 🌐 HTML/CSS | CSS — Responsivo & Moderno | Responsividade · Custom Properties · Cascade avançado | `html-03-responsivo-moderno.html` |
| `10-HTML-04` | `[x]` | 🌐 HTML/CSS | CSS — Animações, Tipografia & Efeitos | Animações & Transições · Typography · Transforms & 3D · Gradients & filters | `html-04-animacoes-efeitos.html` |
| `11-GH-03` | `[x]` | 🐙 GitHub | GitHub — Colaboração & Pull Requests | Remote & Push/Pull · Pull Requests · Issues & Projects · README & Docs | `gh-03-colaboracao-prs.html` |
| `12-JS-01` | `[x]` | ⚡ JavaScript | JavaScript — Core & DOM | Tipos & variáveis · Funções · DOM & eventos · Escopo & hoisting | `js-01-core-dom.html` |

---

## 🟨 PRIORIDADE 3 — INTERMEDIÁRIO TRANSVERSAL
> Habilidades que aparecem em todas as trilhas avançadas.
> Referência: Semanas 9–12 do roadmap.

| ID | Status | Trilha | Título da Aula | Cards agrupados | Arquivo |
|---|---|---|---|---|---|
| `13-JS-02` | `[x]` | ⚡ JavaScript | JavaScript — Objetos, Arrays & ES6+ | Objetos & arrays · Prototype chain · Modules · Classes | `js-02-objetos-es6.html` |
| `14-JS-03` | `[x]` | ⚡ JavaScript | JavaScript — Async: Event Loop, Promises & Fetch | Event Loop · Promises · Async/Await · Fetch API | `js-03-async-promises.html` |
| `15-PY-05` | `[x]` | 🐍 Python | Python — HTTP, APIs & Bibliotecas Essenciais | requests · pathlib/os · datetime · regex | `py-05-http-bibliotecas.html` |
| `16-GH-04` | `[ ]` | 🐙 GitHub | Git Avançado — Rebase, Tags & Estratégias | Rebase · Estratégias de branch · Tags · Releases | `gh-04-git-avancado.html` |
| `17-DKR-01` | `[ ]` | 🐳 Docker | Docker — Conceitos, Imagens & Containers | Conceitos · Comandos core · Volumes | `dkr-01-conceitos-containers.html` |
| `18-DKR-02` | `[ ]` | 🐳 Docker | Docker — Dockerfile & Boas Práticas | Dockerfile · Image optimization · Health checks · Segurança | `dkr-02-dockerfile.html` |

---

## 🟩 PRIORIDADE 4 — STACK PROFISSIONAL
> Ferramentas que engenheiros usam no dia a dia em produção.
> Referência: Semanas 13–16 do roadmap.

| ID | Status | Trilha | Título da Aula | Cards agrupados | Arquivo |
|---|---|---|---|---|---|
| `19-DKR-03` | `[ ]` | 🐳 Docker | Docker Compose & Redes | Docker Compose · Networking · Environment · Multi-stage builds | `dkr-03-compose-redes.html` |
| `20-GH-05` | `[ ]` | 🐙 GitHub | GitHub Actions — CI/CD Completo | Workflows & YAML · CI testes automáticos · CD deploy · Secrets · Marketplace | `gh-05-actions-cicd.html` |
| `21-N8N-01` | `[ ]` | 🔀 n8n | n8n — Setup & Primeiro Workflow | Instalação · Interface · Primeiro workflow · Tipos de triggers | `n8n-01-setup-workflow.html` |
| `22-N8N-02` | `[ ]` | 🔀 n8n | n8n — Nodes Essenciais & Lógica | HTTP Request · Code Node · IF/Switch · Loop · Merge & Set · Error Trigger | `n8n-02-nodes-logica.html` |
| `23-JS-04` | `[ ]` | ⚡ JavaScript | TypeScript — Tipos, Interfaces & Generics | Tipos & interfaces · Strict mode · Utility types · Decorators | `js-04-typescript.html` |
| `24-HTML-05` | `[ ]` | 🌐 HTML/CSS | CSS Tooling — Tailwind, Sass & Figma | Tailwind CSS · Sass/SCSS · PostCSS · Figma → Código | `html-05-tooling.html` |

---

## 🟦 PRIORIDADE 5 — BACK-END & DADOS
> APIs, bancos de dados e Python profissional.
> Referência: Semanas 17–20 do roadmap.

| ID | Status | Trilha | Título da Aula | Cards agrupados | Arquivo |
|---|---|---|---|---|---|
| `25-PY-06` | `[ ]` | 🐍 Python | Python — pandas & NumPy | pandas · NumPy · análise exploratória de dados | `py-06-pandas-numpy.html` |
| `26-PY-07` | `[ ]` | 🐍 Python | FastAPI — API REST do Zero | FastAPI · Pydantic · validação · async · Swagger | `py-07-fastapi.html` |
| `27-PY-08` | `[ ]` | 🐍 Python | Python Back-end Completo | SQLAlchemy · Autenticação JWT · Async/Await · pytest · Deploy | `py-08-backend-completo.html` |
| `28-JS-05` | `[ ]` | ⚡ JavaScript | Node.js & Express — API REST | Node.js · Express/Fastify · rotas · middleware · REST API | `js-05-nodejs-express.html` |
| `29-N8N-03` | `[ ]` | 🔀 n8n | n8n — Integrações Reais | Google Sheets · Telegram/Slack · Email · Banco de dados · Airtable/Notion | `n8n-03-integracoes.html` |
| `30-GH-06` | `[ ]` | 🐙 GitHub | GitHub Avançado — Segurança & Packages | Branch protection · Dependabot · Code scanning · Packages & Registry · API & CLI | `gh-06-seguranca-packages.html` |

---

## 🟪 PRIORIDADE 6 — FULL-STACK & ORQUESTRAÇÃO
> React, Next.js, Kubernetes e automações avançadas.
> Referência: Semanas 19–22 do roadmap.

| ID | Status | Trilha | Título da Aula | Cards agrupados | Arquivo |
|---|---|---|---|---|---|
| `31-JS-06` | `[ ]` | ⚡ JavaScript | React 18 — Componentes, Hooks & Estado | React 18+ · JSX · hooks · context · Suspense · Server Components | `js-06-react.html` |
| `32-JS-07` | `[ ]` | ⚡ JavaScript | Next.js — Full-stack Moderno | Next.js · App Router · SSR · SSG · API routes | `js-07-nextjs.html` |
| `33-DKR-04` | `[ ]` | 🐳 Docker | Docker em Produção — Registry & Swarm | Registry · CI/CD com Docker · Docker Swarm | `dkr-04-producao-swarm.html` |
| `34-N8N-04` | `[ ]` | 🔀 n8n | n8n Avançado — Sub-workflows & Self-hosting | Sub-workflows · Self-hosting · Custom nodes | `n8n-04-avancado.html` |
| `35-GH-07` | `[ ]` | 🐙 GitHub | GitHub no Stack Completo | GitHub + Docker · GitHub + n8n · GitHub + Python · GitHub Pages · Monorepo | `gh-07-stack-completo.html` |
| `36-HTML-06` | `[ ]` | 🌐 HTML/CSS | Acessibilidade & SEO | Acessibilidade · ARIA · SEO básico · Pseudo-elementos · Figma handoff | `html-06-a11y-seo.html` |

---

## 🔴 PRIORIDADE 7 — INTELIGÊNCIA ARTIFICIAL
> O core da trilha de IA. Prereq: Python back-end + APIs.
> Referência: Semanas 19–24 do roadmap.

| ID | Status | Trilha | Título da Aula | Cards agrupados | Arquivo |
|---|---|---|---|---|---|
| `37-AI-01` | `[ ]` | 🤖 IA | Como LLMs Funcionam | Como LLMs funcionam · tokens · context window · temperature · top-p/top-k | `ai-01-como-llms-funcionam.html` |
| `38-AI-02` | `[ ]` | 🤖 IA | Prompt Engineering — Fundamentos | zero-shot · few-shot · CoT · role prompting · system vs user prompt | `ai-02-prompt-eng-fundamentos.html` |
| `39-AI-03` | `[ ]` | 🤖 IA | Prompt Engineering — Avançado | Tree-of-Thought · Self-Consistency · ReAct · chaining · JSON mode · meta-prompting · jailbreak defense | `ai-03-prompt-eng-avancado.html` |
| `40-AI-04` | `[ ]` | 🤖 IA | APIs de LLM — OpenAI, Anthropic & Gemini | chamadas básicas · streaming · autenticação · Avaliação de respostas | `ai-04-apis-llm.html` |
| `41-N8N-05` | `[ ]` | 🔀 n8n | n8n + IA — AI Agent Node & LLMs | OpenAI/Anthropic no n8n · AI Agent node · memory · RAG pipelines | `n8n-05-ia-agentes.html` |

---

## 🔵 PRIORIDADE 8 — RAG & AGENTES
> O coração da engenharia de IA aplicada.
> Referência: Semanas 23–28 do roadmap.

| ID | Status | Trilha | Título da Aula | Cards agrupados | Arquivo |
|---|---|---|---|---|---|
| `42-AI-05` | `[ ]` | 🤖 IA | Embeddings & Vector Stores | Embeddings · similaridade cosseno · Pinecone/Chroma/Qdrant/pgvector | `ai-05-embeddings-vectorstores.html` |
| `43-AI-06` | `[ ]` | 🤖 IA | Pipeline RAG Completo | Chunking · ingestão → busca → rerank → geração · Avaliação de RAG · RAGAS | `ai-06-rag-pipeline.html` |
| `44-AI-07` | `[ ]` | 🤖 IA | Agentes — Function Calling, ReAct & Memória | Function Calling · ReAct pattern · Memória · LangChain · LlamaIndex · Assistants API | `ai-07-agentes-tools.html` |
| `45-DKR-05` | `[ ]` | 🐳 Docker | Kubernetes & Helm | Kubernetes básico · pods · deployments · services · ingress · Helm | `dkr-05-kubernetes-helm.html` |

---

## ⚫ PRIORIDADE 9 — OPENCLAW & PROJETOS FINAIS
> Automação avançada de browser e integração de tudo.
> Referência: Semanas 21–32 do roadmap.

| ID | Status | Trilha | Título da Aula | Cards agrupados | Arquivo |
|---|---|---|---|---|---|
| `46-OC-01` | `[ ]` | 🦀 OpenClaw | Playwright & Fundamentos de Automação | Browser automation · Playwright/Puppeteer · XPath & CSS selectors · HTTP intercept | `oc-01-playwright-fundamentos.html` |
| `47-OC-02` | `[ ]` | 🦀 OpenClaw | OpenClaw — Setup & Tarefas Core | Setup & configuração · Tarefas básicas · Scraping estruturado · Autenticação | `oc-02-setup-core.html` |
| `48-OC-03` | `[ ]` | 🦀 OpenClaw | OpenClaw + IA — Vision & Agentes | Linguagem natural · Vision-based interaction · Agentes de pesquisa · Pipelines automáticos | `oc-03-ia-visao-agentes.html` |
| `49-AI-08` | `[ ]` | 🤖 IA | Multi-Agentes — CrewAI & LangGraph | Autogen/CrewAI · LangGraph · Padrões de design · Avaliação & guardrails | `ai-08-multi-agentes.html` |
| `50-OC-04` | `[ ]` | 🦀 OpenClaw | OpenClaw Avançado + Stack Completo | Anti-bot & detecção · Escalabilidade · Integração n8n · Monitoramento | `oc-04-avancado-stack.html` |

---

## 📊 RESUMO GERAL

| # | Prioridade | Bloco | Aulas | Semanas ref. |
|---|---|---|---|---|
| 1 | 🟥 | Base Universal | 6 | 1–4 |
| 2 | 🟧 | Fundamentos Sólidos | 6 | 5–8 |
| 3 | 🟨 | Intermediário Transversal | 6 | 9–12 |
| 4 | 🟩 | Stack Profissional | 6 | 13–16 |
| 5 | 🟦 | Back-end & Dados | 6 | 17–20 |
| 6 | 🟪 | Full-stack & Orquestração | 6 | 19–22 |
| 7 | 🔴 | Inteligência Artificial | 5 | 19–24 |
| 8 | 🔵 | RAG & Agentes | 4 | 23–28 |
| 9 | ⚫ | OpenClaw & Projetos Finais | 5 | 21–32 |
| | | **TOTAL** | **50** | |

---

## 🔍 Como usar este índice

**Criar uma aula:** Informe o ID. Ex: `"crie a aula 01-GH-01"`.
**Marcar concluída:** Troque `[ ]` por `[x]` na coluna Status.
**Cards linkados:** Cada aula indica quais cards do roadmap recebem badge `▶ Aula`.
**Navegação:** Somente pelo roadmap → clica no card → abre a aula.
Dentro de cada aula: botão `← Roadmap` no topo + rodapé.
