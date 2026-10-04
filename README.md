我做**本地优先的桌面工具**：跨平台阅读器、系统集成组件，以及给 AI agent 与 ComfyUI 用的工作流工具。
I build **local-first desktop tools** — cross-platform readers, OS-integration components, and workflow tooling for AI agents and ComfyUI.

What keeps pulling me in is the layer underneath the UI: archive formats, text decoding, thumbnail pipelines, shell handlers, process supervision. The parts where a tool either works on your actual files or it doesn't.

## Currently

**[grzeb](https://github.com/HibernalGlow/grzeb)** — directory-wide plain-text search that returns a *drill-downable result tree* instead of a flat hit list, with decoded text cached in a local SQLDelight database so a second search over the same files never re-reads disk. One Compose Multiplatform codebase targeting desktop (JVM), Android (SAF), and wasm. Its README leads with what does **not** work yet, which is the fastest way to see how I approach a problem.

## Representative work

| Project | Stack | What it is |
| --- | --- | --- |
| [grzeb](https://github.com/HibernalGlow/grzeb) | Kotlin · Compose Multiplatform · SQLDelight | Tree-shaped full-text search over a whole directory, desktop + Android |
| [Xiranite](https://github.com/HibernalGlow/Xiranite) | React 19 · TypeScript · Wails v3 (Go) · Bun | Desktop workspace host: one capability "node" rendered across six layouts (dashboard, cards, dockview, flow canvas, lanes, bento grid) behind a single contract |
| [neoview](https://github.com/HibernalGlow/neoview) | Tauri 2 · Svelte 5 · Rust · PyO3 | Local image / manga viewer built around a Rust + SQLite thumbnail and directory cache; the target is NeeView's reading feel on a modern stack |
| [rossi](https://github.com/HibernalGlow/rossi) | Flutter · Rust · JS plugin ABI | Manga reader that ships **no content**: each source is one JS file declaring how to list, search, and resolve images |
| [siyuan-damophus](https://github.com/HibernalGlow/siyuan-damophus) | TypeScript · Svelte | SiYuan (思源笔记) plugin: Markdown question banks through scan → index → practice → recover, plus a virtual relation bar between questions and knowledge points |
| [ArcThumbX](https://github.com/HibernalGlow/ArcThumbX) | Rust · Slint | CBZ / CBR / EPUB / FB2 / AZW3 cover thumbnails rendered *inside* Windows Explorer and macOS Finder |

## By domain

Most of these are working forks: upstream license and authorship stay in each README, and each repo's description states what my side changed.

**Readers, archives, and the formats under them**
[exhentai-manga-manager](https://github.com/HibernalGlow/exhentai-manga-manager) (local tag management for downloaded ExHentai works) · [rossi](https://github.com/HibernalGlow/rossi) · [JHenTai](https://github.com/HibernalGlow/JHenTai) · [quivi-t](https://github.com/HibernalGlow/quivi-t) · [neoxide](https://github.com/HibernalGlow/neoxide) · [opencomic-ai-bin](https://github.com/HibernalGlow/opencomic-ai-bin)

**Image and document pipelines**
[Xlchemy](https://github.com/HibernalGlow/Xlchemy) (JPEG XL / AVIF / WebP batch conversion) · [Trimg](https://github.com/HibernalGlow/Trimg) · [czkawka-tauri](https://github.com/HibernalGlow/czkawka-tauri) (dedup) · [FolioX](https://github.com/HibernalGlow/FolioX) (local batch OCR) · [manga-translator-ui](https://github.com/HibernalGlow/manga-translator-ui)

**PDF → Markdown, for study material**
[MineruCustom](https://github.com/HibernalGlow/MineruCustom) (MinerU post-processing: `discarded_blocks` recovery, footnotes, page marks) · [MarkdownWrapper](https://github.com/HibernalGlow/MarkdownWrapper) (`marku`: heading-structure repair and normalization)

**Agent and ComfyUI workflow tooling**
[ComfyUI-Workflow-Studio](https://github.com/HibernalGlow/ComfyUI-Workflow-Studio) (workflow / asset management plus a generation tab) · [ComfyUI-GlowLoader](https://github.com/HibernalGlow/ComfyUI-GlowLoader) · [skilloom](https://github.com/HibernalGlow/skilloom) (agent skills, plus the gate scripts that reject malformed skill output) · [lazypi](https://github.com/HibernalGlow/lazypi) (extensions for the *pi* coding agent) · [omp-decktop](https://github.com/HibernalGlow/omp-decktop) · [auto-continue](https://github.com/HibernalGlow/auto-continue)

**OS integration**
[hibernal](https://github.com/HibernalGlow/hibernal) (on-demand deep hibernation via `pmset`, with a privileged helper) · [ArcThumbX](https://github.com/HibernalGlow/ArcThumbX) · [AppuruPie](https://github.com/HibernalGlow/AppuruPie) (mouse-wheel gesture layer) · [SmartZ](https://github.com/HibernalGlow/SmartZ)

**Distribution**
[homebrew-tap](https://github.com/HibernalGlow/homebrew-tap) — 26 casks for niche macOS GUI apps that aren't in `homebrew/cask`:

```bash
brew tap hibernalglow/tap
```

[Extras-Glow](https://github.com/HibernalGlow/Extras-Glow) is the same idea for Scoop on Windows.

## How I work

- **Fork and extend, don't rewrite.** Much of my real output sits on forks, tracked against upstream rather than abandoned at a snapshot: siyuan-damophus, Extras-Glow, rossi, Xlchemy, ComfyUI-Workflow-Studio, ArcThumbX. When I port a fix I take the upstream's *conditions*, not only its code — a merge must not silently drop either side.
- **CJK correctness is a requirement, not a nice-to-have.** Chinese text is where most "it works" claims fall apart, so the detection order gets specified and argued: BOM → NUL probe → UTF-8 → GB18030 behind two guards → Latin-1 last. Whole-word matching deliberately does not apply to CJK, because `\b` can never form on either side of a Chinese word.
- **Documents state limits before features.** The write-ups I'm happiest with say what is *not* implemented, why, and which behaviour exists in the core but still has no UI switch.
- **Local-first by default.** Files stay on disk, indexes stay in a local database, inference runs on the machine.

---

No contribution graphs or trophy cards here — stars mostly count zero and some projects are weeks old. That's a fact about reach, and the READMEs above are the honest substitute.
