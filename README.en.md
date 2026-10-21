<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="HibernalGlow: I turn real files into tools that run locally and can be checked. The illustration shows source documents flowing into a working desktop app."
</p>

<p align="center">
  <a href="README.md"><b>中文</b></a> · <b>English</b>
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

I build tools I use myself: pipelines for documents and study material, output gates for AI agents, cross-platform desktop apps. I work on a Mac and a Windows machine every day, so cross-platform is a requirement, not a feature; I like modular, plugin-based systems, so anything that can be split off gets split off; and I care about the interface — MD3 Expressive is the direction I push toward.

Most of these started the same way: something hurt, I told the author, and they either said no or had no time for it. So I did it myself.

What actually holds my attention is the layer under the interface: archive formats, text decoding, thumbnail pipelines, shell handling, process watchdogs. A tool either works on your real files or it does not.

---

<img src="./assets/readme/section-work.svg" width="100%" alt="Selected work · 代表作品">

| Project | Stack | What it is |
| --- | --- | --- |
| [MineruCustom](https://github.com/HibernalGlow/MineruCustom) | Python · MinerU | Post-processing from PDF to Markdown. 8 stars, one from MinerU maintainer [myhloli](https://github.com/myhloli) |
| [skilloom](https://github.com/HibernalGlow/skilloom) | Python | 22 agent skills plus 10 gate and validator scripts that reject malformed output |
| [neoview](https://github.com/HibernalGlow/neoview) | Tauri 2 · Svelte 5 · Rust · PyO3 | Local-first image / manga reader with a Rust + SQLite thumbnail and directory cache; 2,828 commits |
| [grzeb](https://github.com/HibernalGlow/grzeb) | Kotlin · Compose Multiplatform · SQLDelight | Directory-wide full-text search that returns a drill-downable result tree; its README states what does not work yet |
| [Xaihi](https://github.com/HibernalGlow/Xaihi) | TypeScript · DeepSeek Harness | Workbench extension layer: 27 domain nodes, each with its own backend actions, parameter list and panel, shipped as legitimate plugin bundles — the host is not forked |
| [siyuan-damophus](https://github.com/HibernalGlow/siyuan-damophus) | TypeScript · Svelte | SiYuan question-bank plugin: scan → index → practice → recover; 710 commits on my branch against 512 upstream |
| [rossi](https://github.com/HibernalGlow/rossi) | Flutter · Rust · JS plugin ABI | A reader that ships no content: each source is one JS file declaring how to list, search and resolve images, run in a QuickJS sandbox on the Rust side · 2 stars |
| [ArcThumbX](https://github.com/HibernalGlow/ArcThumbX) | Rust · Slint | CBZ / CBR / EPUB / FB2 / AZW3 cover thumbnails rendered inside Windows Explorer and macOS Finder · 2 stars |
| [Xlchemy](https://github.com/HibernalGlow/Xlchemy) | Python · release builds | Batch JPEG XL / AVIF / WebP conversion. Fork of `xl-converter`, 11 releases: added the macOS Apple Silicon package upstream never built, removed the installer's dependency on the build machine's Homebrew |
| [czkawka-tauri](https://github.com/HibernalGlow/czkawka-tauri) | Tauri 2 · TypeScript | Desktop front end for duplicate / similar-image cleanup. Fork, 9 releases, my own Windows build, plus custom theme management and a Taskfile task set |
| [hibernal](https://github.com/HibernalGlow/hibernal) | Swift | On-demand deep hibernation from the menu bar (`pmset` + privileged helper). Upstream stopped at `v1.4.5`; I took it to 2.0.0 and shipped a dmg |

<img src="./assets/readme/section-domain.svg" width="100%" alt="By domain · 领域索引">

What follows is a mix of forks and original work; where a repository is a fork, upstream license and authorship stay in its README, and each repo's description states what my side changed.

**Documents and study material**
[MineruCustom](https://github.com/HibernalGlow/MineruCustom) · [MarkdownWrapper](https://github.com/HibernalGlow/MarkdownWrapper) · [siyuan-damophus](https://github.com/HibernalGlow/siyuan-damophus) · [InkLoom](https://github.com/HibernalGlow/InkLoom) (legal-notes site with Remotion explainers embedded in the page; retired)

**Agent and ComfyUI workflows**
[skilloom](https://github.com/HibernalGlow/skilloom) · [ComfyUI-Workflow-Studio](https://github.com/HibernalGlow/ComfyUI-Workflow-Studio) · [ComfyUI-GlowLoader](https://github.com/HibernalGlow/ComfyUI-GlowLoader) · [lazypi](https://github.com/HibernalGlow/lazypi) · [omp-decktop](https://github.com/HibernalGlow/omp-decktop) · [auto-continue](https://github.com/HibernalGlow/auto-continue)

**Readers, archives, and the formats under them**
[rossi](https://github.com/HibernalGlow/rossi) · [neoview](https://github.com/HibernalGlow/neoview) · [quivi-t](https://github.com/HibernalGlow/quivi-t) · [neoxide](https://github.com/HibernalGlow/neoxide) · [opencomic-ai-bin](https://github.com/HibernalGlow/opencomic-ai-bin)

**Image and document pipelines**
[Xlchemy](https://github.com/HibernalGlow/Xlchemy) (batch JPEG XL / AVIF / WebP) · [Trimg](https://github.com/HibernalGlow/Trimg) · [czkawka-tauri](https://github.com/HibernalGlow/czkawka-tauri) (dedup) · [FolioX](https://github.com/HibernalGlow/FolioX) (local batch OCR) · [manga-translator-ui](https://github.com/HibernalGlow/manga-translator-ui)

**Search and local data**
[grzeb](https://github.com/HibernalGlow/grzeb) (Kotlin · Compose Multiplatform: directory-wide full-text search with a drill-downable result tree, decoded text cached in SQLDelight)

**Developer tooling and automation**
[aestivus](https://github.com/HibernalGlow/aestivus) (Tauri + SvelteKit + FastAPI: drag-and-drop orchestration for Python tool chains, calling the system Python) · [TaskGui](https://github.com/HibernalGlow/TaskGui) (parses `Taskfile.yml`, lists tasks as cards, runs them serially or in parallel) · [PresetUI](https://github.com/HibernalGlow/PresetUI) (terminal preset pickers on rich / textual, prototype) · [trename](https://github.com/HibernalGlow/trename) (AI image tagging CLI with WD14 / MD-Danbooru, GPU-accelerated)

**OS integration**
[hibernal](https://github.com/HibernalGlow/hibernal) (on-demand deep hibernation via `pmset`, with a privileged helper) · [Shiin](https://github.com/HibernalGlow/Shiin) (gamepad-combo screenshots and OBS instant replay, Windows / macOS) · [ArcThumbX](https://github.com/HibernalGlow/ArcThumbX) · [AppuruPie](https://github.com/HibernalGlow/AppuruPie) (mouse-wheel gesture layer) · [SmartZ](https://github.com/HibernalGlow/SmartZ)

**Distribution**
[homebrew-tap](https://github.com/HibernalGlow/homebrew-tap) — 24 casks for niche macOS GUI apps that are not in `homebrew/cask`:

```bash
brew tap hibernalglow/tap
```

[Extras-Glow](https://github.com/HibernalGlow/Extras-Glow) is the same idea for Scoop on Windows.

<img src="./assets/readme/section-law.svg" width="100%" alt="Law × AI · 法律 × AI">

Law undergraduate (class of 2027), with an internship at a law firm. Real legal work looks like this: parties send photos and chat screenshots as evidence, and a document revision means emailing yet another version of the file. A case search without a case number gets treated as AI-generated on sight.

Those two facts set the trade-offs in my document tooling: first turn material into structured Markdown that carries page marks, so every conclusion can be traced back to the exact page; then put AI output through gates, so anything failing structure or semantics never lands. The model drafts and organises; provenance and conclusions still need a human back at the original source. I built one site around exactly that chain, with the animations sitting next to the notes ([InkLoom](https://github.com/HibernalGlow/InkLoom), retired).

<img src="./assets/readme/section-method.svg" width="100%" alt="How I work · 我怎么做事">

- **Both forks and original work.** The fork side keeps tracking upstream: siyuan-damophus, Extras-Glow, rossi, Xlchemy, czkawka-tauri, hibernal, ComfyUI-Workflow-Studio and ArcThumbX are maintained against upstream rather than left at a snapshot; when I port a fix I take the upstream's *conditions*, not only its code, so a merge never silently drops either side. The original side — MineruCustom, skilloom, neoview, grzeb, Xaihi — started from an empty repository, with interfaces and acceptance criteria defined from scratch.
- **Gates before promises.** A generative tool has to be able to judge whether its output is right: structure, semantics, traceability. Otherwise it just moves errors faster.
- **CJK correctness.** Chinese text is where most "it works" claims fall apart, so the detection order gets specified: BOM → NUL probe → UTF-8 → GB18030 behind two guards → Latin-1 last. Whole-word matching does not apply to CJK because `\b` never forms around Chinese words.
- **Documents state limits before features.** The write-ups I'm happiest with say what is *not* implemented, why, and which behaviour exists in the core but still has no UI switch.
- **Local-first by default.** Files stay on disk, indexes stay in a local database, inference runs on the machine.

---

No contribution graphs or trophy cards here. Most of these have single-digit stars and some are weeks old — that's a fact about reach, and the READMEs above are the honest substitute.
