# EN 仓库同步 CN 仓库计划（plan-sync）

> 核心目标：把 EN 仓库从 CN@93a9d27（2026-02-07，即翻译锚点）快照同步到 CN@HEAD（27efbab，2026-08-01），保持目录结构、章节内容与代码逻辑与 CN 一致，同时维持 EN 的英文翻译与 `-en` 链接一致性。

## 一、背景与锚点

- **锚点 commit**：CN `93a9d27`（2026-02-07 19:14）。判定依据：
  - EN 全部 14 章 notebook 的代码单元结构与该 commit 完全一致（EN 比 CN HEAD 各多 1 个末尾空代码单元）；
  - EN 首提交的 `app/app.py` 中 `subagent:search-brief` 与 CN@93a9d27 相同（EN 于 02-14 20:15 自行修复为 `subagent_search_brief`，CN 于 20:18 的 `4ec7a63` 才做同样修复）；
  - notebook 内容在 93a9d27 → 4ec7a63（02-14 20:18，EN 创建当晚 CN 最后一次提交）之间未变。
- **同步目标**：CN `HEAD` = `27efbab`（2026-08-01）。

## 二、用户已确认的范围决定

1. **skills/**：完整翻译同步（`SKILL.md` 翻译 + references 由 EN notebook 自动生成 + scripts 复制）
2. **app/**：全量同步代码（保留 EN 特有英文文档；代码注释保持中文不译，与既有翻译原则一致）
3. **tests/** → **examples/**：跟随 CN 重命名

## 三、工作流（按依赖顺序执行）

### 阶段 1 — 核心 notebook 结构对齐（最低翻译量）

对每个 notebook，应用 CN@93a9d27 → CN@HEAD 的 cell 级变更到 EN 版本：

| 章节 | CN 变更 | EN 动作 |
|------|---------|--------|
| 1.quickstart | `agent_invoke` 简化（删 `content, last_node` 跟踪变量及尾部逻辑） | 应用相同代码改动 |
| 2.stategraph | 删末尾空代码 cell | 删末尾空 cell |
| 3.middleware | 删末尾空代码 cell | 删末尾空 cell |
| 4.human_in_the_loop | 删末尾空代码 cell | 删末尾空 cell |
| 5.memory | 删末尾空 cell + 删重复的 `from langchain.agents import create_agent` | 删末尾空 cell + 删 import |
| 6.context | 删末尾空 cell + 2 处微调（import 路径、`except Exception as e`→`except Exception`） | 删末尾空 cell + 应用微调 |
| 7.mcp_server | 删末尾空代码 cell | 删末尾空 cell |
| 8.supervisor | 删末尾空 cell + 删 `from langchain.agents.middleware import dynamic_prompt, ModelRequest` | 删末尾空 cell + 删 import |
| 9.parallelization | 删末尾空代码 cell | 删末尾空 cell |
| 10.rag | 删末尾空代码 cell | 删末尾空 cell |
| 11.web_search | 删末尾空代码 cell | 删末尾空 cell |
| 12.deep_agents | 无变化 | 无动作 |
| 13.gradio_app | 部署章节 markdown 更新 | 把更新的中文内容翻译为英文后应用 |
| 14.langgraph_cli | 删末尾空代码 cell | 删末尾空 cell |
| book/home.ipynb | 小改 | 同步并翻译 |

- **执行技巧**：EN 各章最后一个 cell 即空代码 cell（已确认），删除即可；微调章节（1,5,6,8）以 CN@HEAD 与 CN@93a9d27 的 cell diff 为准精确应用。
- 参考脚本：`/tmp/nb_diff.py <nb> 93a9d27 HEAD`（运行在 CN 仓库）可随时重放差异。

### 阶段 2 — 根文件同步

| 文件 | 动作 |
|------|------|
| `myst.yml` | 保留 EN 的 `title/description/github`（`-en`），同步其余（favicon 注释等） |
| `README.md` | 应用 CN 更新内容，保留 EN 的 `-en` 链接 |
| `requirements.txt` | 直接复制 CN@HEAD |
| `.env.example` | 同步 |
| `simple_agent.py` | 同步代码 |
| `.gitignore` | 同步（新增 `ruff_cache` 等） |
| `docs/README-en.md` | 从 CN 复制（CN 维护英文版，badge 已指向 `-en`） |

### 阶段 3 — examples/（原 tests/）重命名

- EN：`git mv tests/ examples/`，删除旧 tests 结构
- 同步最新内容：`examples/store.py`（+1 行）、`docker-compose.yml` 等
- 与 CN 的 `examples/` 目录保持一致

### 阶段 4 — app/ 全量同步代码

- **复制 CN@HEAD 代码文件**：`app/app.py`、`tools/`、`utils/`、`prompts/`、`config/`、`mcp/`、`space/`
- **新增**：`app/tests/`（6 个测试文件）、`app/tools/tool_fs.py`、`.dockerignore`
- **更新**：`pyproject.toml`、`uv.lock`、`Dockerfile`、`requirements.txt`、`.python-version`
- **代码注释保持中文不译**（与既有原则一致）
- **文档处理**：
  - `app/README.md`：EN 是英文翻译版 → 把 CN 中文版的更新内容翻译成英文后合并
  - `app/docs/README-en.md`：CN 已是英文，直接同步（4 行 diff）
  - `app/docs/ollama.md`、`query.md`：CN 有更新，翻译后同步
  - 保留 EN 特有文件，检查引用链接（EN `app/README.md` 指向 `./docs/README.md` 的链接需核实修正）

### 阶段 5 — CI 与脚本（零翻译）

- 复制 `.github/workflows/ci.yml`
- 复制 `create_references.sh`

### 阶段 6 — skills/ 完整翻译

- 复制 `skills/dive-into-langgraph/scripts/`（代码，不译）
- **编写英文 `SKILL.md`**：翻译中文部分（frontmatter `name` 保持 `dive-into-langgraph`），链接指向 EN 仓库 / EN 在线文档
- **自动生成 references**：在 EN 仓库运行 `./create_references.sh`，用已翻译的英文 notebook 生成 `references/1-11章.md`（脚本用 `jupyter nbconvert --to markdown`，图片引用替换为 `<!-- IMAGE: ... -->` 注释）
- **校对**：检查生成文件中的残留中文与图片占位符

### 阶段 7 — 验证收尾

- 目录结构 diff：EN vs CN@HEAD（排除 EN 特有工作文档 `docs/plan*.md`、`docs/note.md`）
- 14 章 notebook + `book/home.ipynb` 均能通过 JSON 解析、正常打开
- 章节 cell 数一致（EN == CN HEAD）
- 术语一致性：沿用 `docs/plan.md` 术语表
- 链接检查：所有 `-en` 链接正确、无指向 `dive-into-langgraph` 主仓库的残留（除有意保留的引用）

## 四、一致性原则（复用原翻译计划）

1. **纯同步**：只对齐结构、代码与文本更新，不新增功能
2. 代码逻辑完全照搬 CN；只翻译 markdown/文本
3. 代码注释：app 等代码文件的中文注释不译；notebook 中已译注释保持现状
4. EN 特有内容（英文 README、`-en` 链接）保留并应用更新

## 五、备注

- EN 仓库 `docs/plan.md` 为已完成的历史翻译计划，保留不动
- 同步完成后建议提交为多个逻辑 commit（阶段划分），便于回溯

---

## 六、执行状态（2026-08-01）

✅ 全部阶段已完成（64 个文件变更）：

| 阶段 | 状态 | 说明 |
|------|------|------|
| 1 notebook 对齐 | ✅ | 11 章删末尾空 cell；1/5/6/8 章代码微调（其中 1.quickstart 的 `agent_invoke` 因 EN 为自洽的 display 实现，**不适用** CN 的死变量删除）；13 章 3.10→3.13；book 新增 Acknowledgments |
| 2 根文件 | ✅ | requirements.txt 复制；.gitignore 合并；README 新增 News/Star History/badge；myst.yml、simple_agent.py、.env.example 保持 EN 英文版 |
| 3 examples/ | ✅ | `git mv tests/ examples/`，store.py 加 `cd examples`，docker-compose 注释更新 |
| 4 app/ | ✅ | 代码全量复制 CN@HEAD（注释为中文）；新增 tests/×6、tool_fs.py、.dockerignore；app/README.md 应用 CN 更新（英文）；docs/README-en.md 直接同步；ollama/query/mcp-server-chart/food 因 CN 未改动而保留 EN 英文 |
| 5 CI/脚本 | ✅ | 复制 ci.yml、create_references.sh；deploy-book.yml 升级 action 版本（保留 EN 的 BASE_URL） |
| 6 skills/ | ✅ | 复制 scripts/；翻译 SKILL.md；用 create_references.sh 从 EN notebook 生成英文 references（11 章） |
| 7 验证 | ✅ | 15 notebook JSON 有效；cell 结构与 CN@HEAD 一致；编辑的代码 cell 语法校验通过；文件树差异仅剩有意保留项 |

**有意保留的差异**：
- `docs/README-en.md`：EN 根 README 已是英文，不引入冗余的英文副本
- `docs/plan*.md`、`docs/note.md`、`CLAUDE.md`：EN 工作文档
- app 代码注释为中文（用户决定：代码注释不译）
- EN 的 `-en` 链接、`luochang.ink`/`github.io` 在线书链接、`myst.yml` 标题

**待办建议**：
- 提交变更（建议按阶段拆分为多个 commit）
- 运行 `app` 测试验证代码（`cd app && uv sync --dev --locked && uv run python -m unittest`）

---

## 七、Notebook 执行记录（2026-08-01，uv 项目级环境）

**环境**：根目录新建 `pyproject.toml` + `uv.lock`（依赖取自 requirements.txt，Python 3.13），`.venv` 本地隔离；dev 组含 `jupyter`、`ipykernel`、`rank-bm25`。已注册 `py313` 内核（指向 .venv，供 kernelspec=py313 的 notebook 使用）。

**运行方式**：`.venv/bin/python -m jupyter nbconvert --to notebook --execute --inplace`，PATH 前置 .venv。

| 章节 | 结果 |
|------|------|
| 1,2,3,4,5,9,10,12 | ✅ 跑通，0 错误，输出已刷新（含 LLM 调用） |
| 7.mcp_server | ✅ 跑通，0 错误（需先启动 `python -m mcp_server.get_weather_mcp` 于 127.0.0.1:8000） |
| 8.supervisor | ✅ 跑通，0 错误 |
| 13,14 | 无代码 cell，无需运行 |
| **6.context** | ⚠️ 未跑（用户决定）：`inject_file_context` 的 `ipynbname.path()` 在 nbconvert 无头模式抛 IndexError，真实 Jupyter 正常。留待用户交互运行 |
| **11.web_search** | ⚠️ 未跑（用户决定）：cell#7 无条件 `getpass.getpass()` 需交互输入 TAVILY key 且 .env 无该 key。留待用户交互运行 |

**运行中发现并修复的环境问题**：
- `py313` 内核未注册 → 已注册（`ipykernel install --prefix .venv --name py313`）
- `rank_bm25` 缺失（10.rag 需要，CN requirements.txt 遗漏）→ 已加入 pyproject dev 组并安装

**说明**：10.rag 最后 cell `get_relevant_texts` 返回 `[]` 为 LLM 重排判定的正常结果（机制正常）。
