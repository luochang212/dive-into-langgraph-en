# LangGraph English Translation Project Plan

## Core Objectives

Translate 14 chapters of Jupyter Notebook tutorials from Chinese to English in the `archived/dive-into-langgraph/` directory, outputting to the project root directory.

**Working Principles**:
- **Pure Translation Task**: Only translate text content, no need to add new features or modify code logic
- **Faithful to Original Structure**: Maintain the exact same file structure, directory hierarchy, and naming conventions as the original project
- **Minimal Intervention**: Only modify Markdown text content, keep everything else unchanged

---

## Translation Standards

### Glossary
| Chinese | English |
|------|------|
| 智能体 | Agent |
| 状态图 | StateGraph |
| 中间件 | Middleware |
| 人机交互 | Human-in-the-loop (HITL) |
| 记忆/内存 | Memory |
| 上下文工程 | Context Engineering |
| 监督者模式 | Supervisor Pattern |
| 并行化 | Parallelization |
| 向量检索 | Vector Retrieval |
| 混合检索 | Hybrid Retrieval |
| 节点 | Node |
| 边 | Edge |
| 状态 | State |
| 工作流 | Workflow |
| 工具调用 | Tool Calling |

### Format Preservation Principles
- Preserve all Markdown formatting (headers, lists, code blocks, etc.)
- Preserve all code block content unchanged (including comments, unless the comments themselves need translation)
- Preserve Jupyter Notebook cell structure
- Preserve image links and relative paths
- Preserve YAML frontmatter

### File Naming
- Notebook files keep original filenames
- Output README.md is the English version

---

## Source File List (15 files total)

| No. | Source File | Target Location | Chapter Topic | Status |
|------|--------|----------|----------|------|
| 0 | `archived/dive-into-langgraph/book/home.ipynb` | `./book/home.ipynb` | Home/Table of Contents | ✅ Completed |
| 1 | `archived/dive-into-langgraph/1.quickstart.ipynb` | `./1.quickstart.ipynb` | Quick Start | ✅ Completed |
| 2 | `archived/dive-into-langgraph/2.stategraph.ipynb` | `./2.stategraph.ipynb` | StateGraph | ✅ Completed |
| 3 | `archived/dive-into-langgraph/3.middleware.ipynb` | `./3.middleware.ipynb` | Middleware | ✅ Completed |
| 4 | `archived/dive-into-langgraph/4.human_in_the_loop.ipynb` | `./4.human_in_the_loop.ipynb` | Human-in-the-loop | ✅ Completed |
| 5 | `archived/dive-into-langgraph/5.memory.ipynb` | `./5.memory.ipynb` | Memory | ✅ Completed |
| 6 | `archived/dive-into-langgraph/6.context.ipynb` | `./6.context.ipynb` | Context Engineering | ✅ Completed |
| 7 | `archived/dive-into-langgraph/7.mcp_server.ipynb` | `./7.mcp_server.ipynb` | MCP Service | ✅ Completed |
| 8 | `archived/dive-into-langgraph/8.supervisor.ipynb` | `./8.supervisor.ipynb` | Supervisor Pattern | ✅ Completed |
| 9 | `archived/dive-into-langgraph/9.parallelization.ipynb` | `./9.parallelization.ipynb` | Parallelization | ✅ Completed |
| 10 | `archived/dive-into-langgraph/10.rag.ipynb` | `./10.rag.ipynb` | RAG | ✅ Completed |
| 11 | `archived/dive-into-langgraph/11.web_search.ipynb` | `./11.web_search.ipynb` | Web Search | ✅ Completed |
| 12 | `archived/dive-into-langgraph/12.deep_agents.ipynb` | `./12.deep_agents.ipynb` | Deep Agents | ✅ Completed |
| 13 | `archived/dive-into-langgraph/13.gradio_app.ipynb` | `./13.gradio_app.ipynb` | Gradio App | ✅ Completed |
| 14 | `archived/dive-into-langgraph/14.langgraph_cli.ipynb` | `./14.langgraph_cli.ipynb` | LangGraph CLI | ✅ Completed |

---

## Workflow

### Phase 1: Preparation
- [x] Check source file integrity
- [x] Create output directory structure (`book/` directory, etc.)
- [x] Familiarize with glossary

### Phase 2: Chapter-by-Chapter Translation (in numerical order)
For each notebook:
1. [x] Read source file content
2. [x] Translate Chinese text in Markdown cells to English
3. [x] Preserve all code blocks, comments, and image links unchanged
4. [x] Save to target location
5. [x] Verify file can open normally
6. [x] Mark as completed in progress table

### Phase 3: Translate README
- [x] Translate root directory README.md to English version
- [x] Update directory structure and links

### Phase 4: Final Verification
- [x] Batch check all notebooks can open normally
- [x] Batch check terminology consistency
- [x] Verify image links are valid and files exist
- [x] Compare source and output file counts are consistent

---

## Execution Strategy

### Subagent Usage Limits
- **Maximum 3 subagents running simultaneously** to avoid excessive resource consumption
- Each subagent handles independent file translation tasks
- Prioritize using `NotebookEdit` tool to directly edit notebook files

### Translation Order Recommendation
1. Translate `book/home.ipynb` first (table of contents home page)
2. Translate chapters 1-14 in numerical order
3. Finally translate `README.md`

### Resource Handling
- **Images**: Image files from the original project need to be copied from `archived/dive-into-langgraph/` to the corresponding output directory, maintaining relative paths
- **Data files**: If there are example data files, copy them to the output directory as well

---

## QA Checklist

After each chapter translation is complete, check:
- [ ] All Markdown text has been translated to English
- [ ] Code blocks remain unchanged (including Chinese comments)
- [ ] Jupyter Notebook cell structure is intact
- [ ] Image link paths are correct, image files have been copied
- [ ] File can be opened normally with Jupyter
- [ ] Terminology translation is consistent (refer to glossary)

---

## Notes

1. **Pure Translation**: Only translate Markdown text, do not modify code or add new features
2. **Code Comments**: Chinese comments in code preserve the original text, no translation needed
3. **Output Cells**: Preserve original output results or clear them (depending on situation)
4. **Project Structure**: Maintain the original project's directory structure and file organization, no refactoring