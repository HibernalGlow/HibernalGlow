<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="HibernalGlow：把文档、笔记和 AI 输出做成在本机运行且可校验的工具。右侧列出三条可核验的事实：MineruCustom 的 7 个外部 Star（含 MinerU 维护者的一星）、neoview 的 2828 次提交、skilloom 的 22 个技能与 10 个输出门禁；底部是一条处理链路：资料、带页码的 Markdown、门禁、可回查的交付。"
</p>

<p align="center">
  <b>中文</b> · <a href="README.en.md">English</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust">
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin">
  <img src="https://img.shields.io/badge/Tauri_2-24C8D8?style=flat-square&logo=tauri&logoColor=white" alt="Tauri">
  <img src="https://img.shields.io/badge/local--first-by_default-0B1220?style=flat-square" alt="Local-first by default">
  <img src="https://img.shields.io/badge/agent-tooling-38BDF8?style=flat-square" alt="Agent tooling">
</p>

我做**本地优先的工具**：文档与学习资料的流水线、给 AI agent 用的输出门禁，以及跨平台桌面应用。

真正让我着迷的是界面之下那一层：归档格式、文本解码、缩略图管线、shell 处理、进程看护。工具要么能在你真实的文件上跑通，要么就是没跑通。

<img src="./assets/readme/section-work.svg" width="100%" alt="代表作品 · Selected work">

| 项目 | 技术栈 | 是什么 |
| --- | --- | --- |
| [MineruCustom](https://github.com/HibernalGlow/MineruCustom) | Python · MinerU | PDF → Markdown 后处理。7 个外部 Star，其中一星来自 MinerU 维护者 [myhloli](https://github.com/myhloli) |
| [skilloom](https://github.com/HibernalGlow/skilloom) | Python | 22 个 agent 技能 + 10 个门禁与校验脚本，拒绝格式不合规的产物 |
| [neoview](https://github.com/HibernalGlow/neoview) | Tauri 2 · Svelte 5 · Rust · PyO3 | 本地优先的图像 / 漫画阅读器，Rust + SQLite 缩略图与目录缓存；2,828 次提交 |
| [grzeb](https://github.com/HibernalGlow/grzeb) | Kotlin · Compose Multiplatform · SQLDelight | 目录级全文检索，结果树可下钻而不是平铺；README 写明哪些还没做 |
| [Xaihi](https://github.com/HibernalGlow/Xaihi) | TypeScript · DeepSeek Harness | 工作台扩展层：27 个域节点各自带后端动作、参数表与面板，全部以合规插件包接入宿主，不 fork 它 |
| [siyuan-damophus](https://github.com/HibernalGlow/siyuan-damophus) | TypeScript · Svelte | 思源题库插件：扫描 → 索引 → 练习 → 恢复；本地分支 710 次提交，超过上游的 512 次 |
| [rossi](https://github.com/HibernalGlow/rossi) | Flutter · Rust · JS plugin ABI | 不带内容的阅读器：每个图源是一个 JS 文件，声明怎么列表、搜索、取图，Rust 侧 QuickJS 沙箱执行 |
| [ArcThumbX](https://github.com/HibernalGlow/ArcThumbX) | Rust · Slint | 在 Windows 资源管理器 / macOS Finder 里直接渲染 CBZ / CBR / EPUB / FB2 / AZW3 封面 |

**自己出安装包的版本线。** 下面几个跟的是别人的上游，但版本号、构建和安装包在我这一侧：

| 项目 | 我这一侧 | 发版 |
| --- | --- | --- |
| [Xlchemy](https://github.com/HibernalGlow/Xlchemy) | 补上了上游没有的 macOS Apple Silicon 包，修掉安装包对打包机 Homebrew 的依赖，现编 `cjpegli` 补齐 macOS 默认缺的 JPEG 编码器 | 11 次，产物覆盖 macOS / Windows / Linux |
| [czkawka-tauri](https://github.com/HibernalGlow/czkawka-tauri) | 自出 Windows 构建，加自定义主题与设置管理、Taskfile 任务集 | 9 次，`.exe` |
| [hibernal](https://github.com/HibernalGlow/hibernal) | 上游停在 `v1.4.5`（全部 7 次提交），我在其上做到 2.0.0：图标与徽记重做、README 按应用自身的证据重写 | 1 次，`.dmg` |

<img src="./assets/readme/section-domain.svg" width="100%" alt="领域索引 · By domain">

下面既有 fork，也有原创；是 fork 的仓库，上游的许可证与作者归属保留在各自 README 里，每个仓库的描述会写清我这一侧改了什么。

**文档与学习资料**
[MineruCustom](https://github.com/HibernalGlow/MineruCustom) · [MarkdownWrapper](https://github.com/HibernalGlow/MarkdownWrapper) · [siyuan-damophus](https://github.com/HibernalGlow/siyuan-damophus) · [InkLoom](https://github.com/HibernalGlow/InkLoom)（法律笔记站，页内嵌 Remotion 动画讲解；已停更）

**Agent 与 ComfyUI 工作流**
[skilloom](https://github.com/HibernalGlow/skilloom) · [ComfyUI-Workflow-Studio](https://github.com/HibernalGlow/ComfyUI-Workflow-Studio) · [ComfyUI-GlowLoader](https://github.com/HibernalGlow/ComfyUI-GlowLoader) · [lazypi](https://github.com/HibernalGlow/lazypi) · [omp-decktop](https://github.com/HibernalGlow/omp-decktop) · [auto-continue](https://github.com/HibernalGlow/auto-continue)

**阅读器、归档格式与它们底下的东西**
[rossi](https://github.com/HibernalGlow/rossi) · [neoview](https://github.com/HibernalGlow/neoview) · [quivi-t](https://github.com/HibernalGlow/quivi-t) · [neoxide](https://github.com/HibernalGlow/neoxide) · [opencomic-ai-bin](https://github.com/HibernalGlow/opencomic-ai-bin)

**图像与文档管线**
[Xlchemy](https://github.com/HibernalGlow/Xlchemy)（JPEG XL / AVIF / WebP 批量转换） · [Trimg](https://github.com/HibernalGlow/Trimg) · [czkawka-tauri](https://github.com/HibernalGlow/czkawka-tauri)（去重） · [FolioX](https://github.com/HibernalGlow/FolioX)（本地批量 OCR） · [manga-translator-ui](https://github.com/HibernalGlow/manga-translator-ui)

**检索与本地数据**
[grzeb](https://github.com/HibernalGlow/grzeb)（Kotlin · Compose Multiplatform：全目录全文检索，结果树可下钻，解码文本缓存进 SQLDelight）

**开发工具与自动化**
[aestivus](https://github.com/HibernalGlow/aestivus)（Tauri + SvelteKit + FastAPI：把 Python 工具链做成拖拽编排，直接调用系统 Python） · [TaskGui](https://github.com/HibernalGlow/TaskGui)（解析 `Taskfile.yml`，任务列成卡片，串行 / 并行执行） · [PresetUI](https://github.com/HibernalGlow/PresetUI)（rich / textual 写的终端预设选择器，原型） · [trename](https://github.com/HibernalGlow/trename)（AI 图片打标 CLI，WD14 / MD-Danbooru，GPU 加速）

**系统集成**
[hibernal](https://github.com/HibernalGlow/hibernal)（`pmset` 深度休眠，带特权 helper） · [Shiin](https://github.com/HibernalGlow/Shiin)（手柄组合键截图与 OBS 即时回放，Windows / macOS） · [ArcThumbX](https://github.com/HibernalGlow/ArcThumbX) · [AppuruPie](https://github.com/HibernalGlow/AppuruPie)（滚轮手势层） · [SmartZ](https://github.com/HibernalGlow/SmartZ)

**分发**
[homebrew-tap](https://github.com/HibernalGlow/homebrew-tap) — 24 个 cask，收纳官方仓库没收录的小众 macOS GUI 应用：

```bash
brew tap hibernalglow/tap
```

[Extras-Glow](https://github.com/HibernalGlow/Extras-Glow) 是同一件事在 Windows / Scoop 上的版本。

<img src="./assets/readme/section-law.svg" width="100%" alt="法律 × AI · Law × AI">

法学本科（2027 届），在律所实习过。真实的法律工作是：当事人材料是拍照和聊天截图，文书靠“改一处发一个新版本”；没有案号的检索结果，会被直接当成 AI 生成的。

这两件事决定了我在文档工具上的取舍：先把资料变成带页码标记的结构化 Markdown，让每一条结论都能翻回原页；再让 AI 的产出过门禁，结构或语义不合格就不放行。模型负责初稿与整理，出处和结论仍要人回到原始来源确认。这套链路我做成过一个站点，笔记旁边直接嵌动画讲解（[InkLoom](https://github.com/HibernalGlow/InkLoom)，已停更）。

<img src="./assets/readme/section-method.svg" width="100%" alt="我怎么做事 · How I work">

- **既有 fork，也有原创。** fork 的那一半继续跟上游走：siyuan-damophus、Extras-Glow、rossi、Xlchemy、czkawka-tauri、hibernal、ComfyUI-Workflow-Studio、ArcThumbX 都对着上游维护，不停在某个快照；移植修复时我带走上游的*成立条件*，不只是它的代码——一次合并不应该悄悄丢掉任何一侧。原创的那一半（MineruCustom、skilloom、neoview、grzeb、Xaihi）从空仓库开始，接口和验收方式自己定。
- **先有门禁，再谈能力。** 生成类工具必须能判断输出对不对：结构、语义、可追溯。否则只是把错误搬得更快。
- **中文正确性是要求。** 大多数”能跑通”的说法会在中文上崩掉，所以编码探测顺序要写清并给出理由：BOM → NUL 探测 → UTF-8 → GB18030（两道前置守卫之后）→ Latin-1 兜底。整词匹配对 CJK 不启用，因为 `\b` 在中文词两侧永远成不了。
- **文档先讲限制，再讲功能。** 我最满意的几份说明写清了哪些*还没实现*、为什么，以及核心里已有但界面上还没有开关的行为。
- **默认本地优先。** 文件留在磁盘上，索引留在本地数据库里，推理跑在本机上。

