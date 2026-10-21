"""Rebuild the standalone profile artwork with Python 3.

Run from any directory: python3 assets/readme/source/build.py
Add --embed to refresh only the gallery HTML and localized section image paths.
One renderer produces one SVG. README HTML owns all project-to-project layout.
"""
from html import escape
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
SHAPES = json.loads((HERE / "expressive-shapes.json").read_text())
SANS = "'Google Sans Flex','Roboto Flex',-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
INK = "#171225"
WHITE = "#ece0ff"
MUTED = "#b1a5c9"
LILAC = "#c3bdfe"
LIME = "#cff992"
NAVY = "#001d32"
BLUE = "#cde5ff"
ORANGE = "#ffb77b"
ROSE = "#ffafd4"
PALE_ROSE = "#ffd8e7"
PLUM = "#3d0026"
PEACH = "#ffdcc2"
MINT = "#e9f5d6"
FOREST = "#335000"


def n(v):
    return f"{v:.2f}".rstrip("0").rstrip(".") or "0"


def txt(x, y, value, size, color, weight=500, mono=False, anchor=None, maxw=None):
    attrs = f' text-anchor="{anchor}"' if anchor else ""
    attrs += f' data-maxw="{maxw}"' if maxw else ""
    attrs += f' font-family="{MONO}"' if mono else ""
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
            f'fill="{color}"{attrs}>{escape(value)}</text>')


def rect(x, y, w, h, color, r=16, stroke=None):
    s = f' stroke="{stroke}" stroke-width="2"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{color}"{s}/>'


def shape(name, cx, cy, size, color, rot=0):
    angle = math.radians(rot)
    co, si = math.cos(angle), math.sin(angle)
    def point(x, y):
        x, y = (x - .5) * size, (y - .5) * size
        return f"{n(cx + x * co - y * si)} {n(cy + x * si + y * co)}"
    cs = SHAPES[name]
    d = "M" + point(*cs[0][:2])
    for c in cs:
        d += "C" + " ".join(point(*c[i:i+2]) for i in (2, 4, 6))
    return f'<path d="{d}Z" fill="{color}"/>'


def line(x1, y1, x2, y2, color, width=5, opacity=1):
    return (f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" '
            f'stroke-width="{width}" stroke-linecap="round" opacity="{opacity}"/>')


def tick(x, y, size, color, width=6):
    return (f'<path d="M{n(x-size*.32)} {n(y)}l{n(size*.22)} {n(size*.22)} '
            f'{n(size*.43)} -{n(size*.47)}" fill="none" stroke="{color}" '
            f'stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>')


def group(body, transform):
    return f'<g transform="{transform}">{"".join(body)}</g>'


def wave(x, y, width, color, amplitude=4, period=32, stroke=6):
    pts = [(x+i*width/100, y+amplitude*math.sin(i*width/100*2*math.pi/period)) for i in range(101)]
    return (f'<path d="M{"L".join(n(a)+" "+n(b) for a,b in pts)}" fill="none" '
            f'stroke="{color}" stroke-width="{stroke}" stroke-linecap="round"/>')


def doc(w, h, title, desc, body, bg, lang="zh-CN", radius=40):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc" '
            f'lang="{lang}" font-family="{SANS}">\n'
            f'<title id="title">{escape(title)}</title>\n<desc id="desc">{escape(desc)}</desc>\n'
            f'<defs><clipPath id="frame">{rect(0,0,w,h,"#fff",radius)}</clipPath></defs>\n'
            f'<g clip-path="url(#frame)">{rect(0,0,w,h,bg,radius)}\n'
            + "\n".join(body) + "\n</g>\n</svg>\n")


def hero(en=False):
    b = [shape("clover4Leaf", 1093, 220, 404, "#211a34", 8),
         shape("sunny", 79, 62, 48, LIME, 8),
         txt(79, 70, "H", 23, INK, 800, anchor="middle"),
         txt(117, 71, "HibernalGlow", 29, WHITE, 750),
         txt(1138, 69, "LAW × CODE", 20, LILAC, 650, mono=True, anchor="end")]
    if en:
        b += [txt(55, 171, "A real itch.", 81, WHITE, 650, maxw=720),
              txt(50, 278, "I build the fix.", 92, LIME, 850, maxw=740),
              txt(60, 338, "Document pipelines · agent gates · desktop apps", 25, WHITE, maxw=750),
              txt(60, 433, "Law undergraduate · 2027", 19, MUTED)]
    else:
        b += [txt(55, 170, "有个痛点。", 80, WHITE, 650, maxw=720),
              txt(49, 279, "那就自己做。", 98, LIME, 850, maxw=745),
              txt(60, 338, "文档流水线 · Agent 输出门禁 · 跨平台桌面应用", 25, WHITE, maxw=760),
              txt(60, 433, "法学本科 · 2027 届", 19, MUTED)]
    # Connected button group: both platforms matter. Static illustration, no controls.
    b += [rect(60, 368, 114, 42, LILAC, 21), tick(80, 389, 20, "#282259", 3),
          txt(99, 396, "macOS", 18, "#282259", 700),
          rect(178, 368, 136, 42, LILAC, 21), tick(199, 389, 20, "#282259", 3),
          txt(219, 396, "Windows", 18, "#282259", 700),
          txt(337, 396, "Local files. Checkable results." if en else "文件在本机，结果能校验。", 22, MUTED, maxw=480)]
    # One personal motif: a real file becomes an inspectable tool. No project cards.
    b += [shape("arch", 1003, 224, 295, LILAC, 10)]
    paper = [rect(0, 0, 144, 187, "#fef7ff", 18),
             txt(20, 43, "PDF", 28, "#3c376e", 800, mono=True),
             line(22, 66, 114, 66, "#c3bdfe", 7),
             line(22, 89, 101, 89, "#c3bdfe", 7),
             line(22, 112, 114, 112, "#c3bdfe", 7),
             line(22, 151, 80, 151, "#b1a5c9", 5)]
    b += [group(paper, "translate(861 122) rotate(-12 72 93)")]
    tool = [rect(0,0,147,173,"#282259",24),
            txt(20,42,">_",33,LILAC,800,mono=True),
            line(22,70,115,70,LILAC,6),line(22,91,92,91,LILAC,6),
            rect(18,116,111,39,LIME,19.5),tick(73,135,34,"#335000",5)]
    b += [group(tool,"translate(988 182) rotate(8 74 86)"),
          shape("softBurst", 1116, 132, 76, ORANGE, 8),
          tick(1116,132,34,"#2e1500",5),
          wave(861,380,264,LILAC,5,45,6)]
    return doc(1200,464,"HibernalGlow — A real itch. I build the fix." if en else "HibernalGlow：有个痛点，那就自己做。",
        "Personal profile: law undergraduate, class of 2027. Builds document pipelines, agent output gates and desktop tools for macOS and Windows. A file and a checked terminal illustrate local, inspectable tools." if en else
        "个人定位：2027 届法学本科，做文档流水线、Agent 输出门禁和跨平台桌面应用，同时使用 macOS 与 Windows。右侧用文件和带勾选标记的终端表现本机运行、结果可校验。hero 内不包含代表项目卡片。",b,INK,"en" if en else "zh-CN",48)


def mineru(en=False):
    b=[txt(32,49,"PDF → MARKDOWN",18,"#3c376e",700,mono=True),
       txt(32,101,"MineruCustom",44,"#282259",800,maxw=516),
       txt(32,141,"Bring footnotes back. Keep page marks." if en else "捡回脚注，找回原页。",24,"#3c376e",600,maxw=516)]
    before=[rect(0,0,150,184,"#fef7ff",18),txt(18,31,"middle.json",16,"#3c376e",650,mono=True),
            line(18,52,127,52,"#b5afef",6),line(18,72,111,72,"#b5afef",6),line(18,92,127,92,"#b5afef",6),
            rect(12,116,126,55,"#ffd8e7",12),txt(24,140,"[^1]",20,"#782955",700,mono=True),
            line(25,155,99,155,"#ef8cbd",5)]
    b += [group(before,"translate(49 184) rotate(-6 75 92)"),
          txt(47,391,"discarded_blocks",16,"#3c376e",600,mono=True)]
    after=[rect(0,0,182,204,"#fef7ff",22),rect(12,12,158,60,"#e9ddff",14),
           txt(25,36,"```page",18,"#3c376e",650,mono=True),
           txt(25,61,"page 42" if en else "第 42 页",22,"#282259",750),
           line(20,95,160,95,"#b5afef",6),line(20,117,141,117,"#b5afef",6),
           rect(12,143,158,46,LIME,14),txt(26,173,"[^1] restored" if en else "[^1] 脚注归位",18,"#335000",650)]
    b += [group(after,"translate(339 171) rotate(4 91 102)"),
          wave(217,267,102,"#3c376e",7,38,5),
          '<path d="M307 254l16 13-16 13" fill="none" stroke="#3c376e" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>',
          shape("sunny",307,198,49,LIME,8),tick(307,198,22,"#335000",3.5),
          txt(32,426,"Python · MinerU post-processing" if en else "Python · MinerU 后处理",18,"#3c376e",600,mono=en),
          txt(548,426,"ILLUSTRATION" if en else "恢复过程示意",14,"#3c376e",500,anchor="end")]
    return doc(580,448,"MineruCustom — restore footnotes and page marks" if en else "MineruCustom：捡回脚注，找回原页",
        "Conceptual before/after, based on the repository's page-42 example: discarded footnotes in middle.json are restored, and Markdown receives a page marker. Original Python project; post-processing after MinerU." if en else
        "根据项目 README 第 42 页示例绘制的恢复过程示意：左侧 middle.json 的 discarded_blocks 中有脚注；右侧 Markdown 补回 page 页码标记并恢复脚注。原创 Python 项目，运行在 MinerU 之后。",b,LILAC,"en" if en else "zh-CN")


def skilloom(en=False):
    b=[txt(32,49,"AGENT OUTPUT GATES",18,LIME,700,mono=True),txt(30,104,"skilloom",50,WHITE,800),
       txt(32,144,"Invalid output? Reject it." if en else "产物不合格，就拒收。",25,WHITE,600,maxw=516),
       rect(30,180,520,180,"#261e39",32),txt(52,215,"legal-marknote",18,MUTED,600,mono=True),
       shape("softBurst",506,188,87,"#fd6f85",8),
       '<path d="M495 177l22 22m0-22-22 22" fill="none" stroke="#490013" stroke-width="6" stroke-linecap="round"/>']
    for y,code,label in [(237,"E411","Table wider than 2 columns" if en else "表格超过 2 列上限"),
                          (283,"E625","Subject has no semantic color" if en else "主体缺少语义颜色")]:
        b += [rect(50,y,80,31,"#8a1632",9),txt(90,y+22,code,18,"#ff97a3",750,mono=True,anchor="middle"),
              txt(144,y+23,label,20 if en else 23,WHITE,500,maxw=380)]
    b += [txt(52,343,"rc=1",18,"#ff97a3",700,mono=True),
          txt(32,419,"22",39,LILAC,800),txt(91,417,"skills" if en else "个技能",20,MUTED,600),
          txt(262,419,"10",39,LIME,800),txt(322,417,"gates & checks" if en else "门禁与校验",20,MUTED,600,maxw=230)]
    return doc(580,448,"skilloom — reject invalid agent output" if en else "skilloom：产物不合格，就拒收",
        "The repository's real rejection example: legal-marknote flags E411 for a table wider than two columns, E625 for a subject without semantic color, and exits with rc=1. 22 skills and 10 gate/validator scripts, as listed in the profile README." if en else
        "取自项目 README 的真实拒收示例：legal-marknote 对超过两列的表格报 E411，对未赋予语义颜色的主体报 E625，退出码 rc=1。底部沿用主页 README 的 22 个技能、10 个门禁与校验脚本口径。",b,INK,"en" if en else "zh-CN")


def neoview(en=False):
    b=[txt(32,49,"LOCAL IMAGE LIBRARY",18,"#004a75",700,mono=True),txt(30,103,"neoview",48,NAVY,800),
       txt(32,142,"Your images. On your machine." if en else "图像与漫画，留在本机。",25,NAVY,600,maxw=516)]
    clips=[]
    for i,(name,cx,fill,ink,rot) in enumerate([
        ("arch",96,LILAC,"#454078",-9),("clover4Leaf",225,LIME,"#3f6007",6),
        ("pill",354,ORANGE,"#6d3900",-12)]):
        s=shape(name,cx,233,115,fill,rot)
        # Reuse the shape's exact path for image clipping, keeping photos conceptual.
        clips.append(f'<clipPath id="thumb{i}">{s}</clipPath>')
        picture=[s,f'<circle cx="{cx+20}" cy="211" r="13" fill="{ink}" opacity=".65"/>',
                 f'<path d="M{cx-65} 282l47-67 27 38 21-24 40 53v30H{cx-65}Z" fill="{ink}" opacity=".82"/>']
        b += [f'<g clip-path="url(#thumb{i})">{"".join(picture)}</g>']
    b += [rect(426,176,113,113,"#b2d7f4",32),shape("cookie9Sided",482.5,232.5,47,"#62b2f3",15),
          '<path d="M483 219a13 13 0 1 1-13 13" fill="none" stroke="#004a75" stroke-width="4" stroke-linecap="round"/>',
          txt(482,315,"queued" if en else "等待生成",17,"#004a75",600,anchor="middle"),
          wave(34,337,330,"#004a75",4,32,6),line(382,337,543,337,"#95bcdc",6),
          '<circle cx="543" cy="337" r="3" fill="#004a75"/>',
          txt(32,391,"Rust + SQLite",28,NAVY,750),
          txt(32,423,"Thumbnail & directory cache" if en else "缩略图与目录缓存",21,"#004a75",550,maxw=510)]
    b.insert(0,"<defs>"+"".join(clips)+"</defs>")
    return doc(580,448,"neoview — a local image and manga reader" if en else "neoview：图像与漫画，留在本机",
        "Conceptual thumbnail cache illustration: three landscape thumbnails and one queued placeholder, with a wavy progress indicator. Local-first image/manga reader, using Rust and SQLite for thumbnail and directory caching." if en else
        "缩略图缓存的概念示意：三张裁切缩略图与一张等待生成的占位图，下方为波浪进度条。本地优先的图像与漫画阅读器，以 Rust 与 SQLite 维护缩略图和目录缓存。",b,BLUE,"en" if en else "zh-CN")


def grzeb(en=False):
    b=[txt(32,49,"DIRECTORY SEARCH",18,FOREST,700,mono=True),
       txt(30,103,"grzeb",50,FOREST,800),
       txt(32,142,"Follow the tree. Find the line." if en else "按目录下钻，直达命中行。",25,FOREST,600,maxw=516),
       rect(30,171,520,48,FOREST,24),
       '<circle cx="58" cy="193" r="9" fill="none" stroke="#e9f5d6" stroke-width="3"/>',
       line(65,200,72,207,MINT,3),
       txt(86,202,"contract" if en else "合同",22,MINT,650),
       txt(53,251,"/workspace",22,FOREST,650,mono=True)]
    b += [line(66,265,66,337,"#93ad72",3),line(66,282,93,282,"#93ad72",3),
          line(66,337,93,337,"#93ad72",3),line(109,296,109,314,"#93ad72",3),
          line(109,314,139,314,"#93ad72",3),
          txt(99,289,"notes/",22,FOREST,650,mono=True),
          rect(146,297,382,38,"#f5ffe8",10),
          txt(161,324,"contract.md",21,FOREST,700,mono=True),
          txt(99,345,"archive/",22,FOREST,550,mono=True),
          shape("slanted",489,276,43,FOREST,-12),
          '<path d="M480 275h17m-8-8 8 8-8 8" fill="none" stroke="#e9f5d6" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
          txt(32,393,"Kotlin · Compose Multiplatform",18,FOREST,650,maxw=516),
          txt(32,424,"Decoded text cached in SQLDelight" if en else "解码后的正文，缓存进 SQLDelight",21,FOREST,550,maxw=516)]
    return doc(580,448,"grzeb — follow a directory search result tree" if en else "grzeb：按目录下钻，直达命中行",
        "Conceptual result tree with example paths /workspace, notes/contract.md and archive/. Searching a directory produces a navigable hierarchy; decoded text is cached in SQLDelight. File names illustrate the mechanism, not a measured search result." if en else
        "结果树机制示意，使用 /workspace、notes/contract.md 与 archive/ 作为示例路径。目录级全文检索支持逐级钻取并跳转命中行，解码后的正文缓存进 SQLDelight；示意路径不代表实测结果。",b,MINT,"en" if en else "zh-CN")


def xaihi(en=False):
    b=[txt(32,49,"WORKBENCH EXTENSIONS",18,LILAC,700,mono=True),
       txt(30,103,"Xaihi",50,WHITE,800),
       txt(32,142,"Domain tools, plugged into the host." if en else "领域工具，以插件接入宿主。",25,WHITE,600,maxw=516),
       rect(31,174,518,54,LILAC,27),
       txt(290,209,"DeepSeek Harness",25,"#282259",750,anchor="middle")]
    # One domain bundle owns all three facets; the host connects to the bundle.
    b += [line(290,228,290,251,LILAC,5),
          '<path d="M107 264v-13h366v13" fill="none" stroke="#7b7091" stroke-width="3" stroke-linejoin="round"/>']
    facets=[(32,"action","动作","#c3bdfe","#282259"),
            (216,"schema","参数",BLUE,NAVY),(400,"panel","面板",LIME,FOREST)]
    for x,english,chinese,fill,ink in facets:
        b += [rect(x,264,148,91,"#29213d",20),rect(x+15,277,118,38,fill,19),
              txt(x+74,304,{"action":">_","schema":"{ }","panel":"▦"}[english],25,ink,800,mono=english!="panel",anchor="middle"),
              txt(x+74,341,english if en else chinese,21,WHITE,650,anchor="middle")]
    b += [txt(32,408,"27",46,LIME,800),
          txt(99,405,"domain nodes" if en else "个域节点",22,WHITE,600),
          txt(547,431,"TypeScript · plugin bundles",17,MUTED,550,anchor="end")]
    return doc(580,448,"Xaihi — domain tools plugged into DeepSeek Harness" if en else "Xaihi：领域工具，以插件接入宿主",
        "Conceptual plugin bundle: DeepSeek Harness connects to backend actions, parameter schemas and workspace panels. The profile and Xaihi README both list 27 domain nodes. This is an architecture illustration, not a screenshot or a host-verification claim." if en else
        "插件包机制示意：DeepSeek Harness 接入后端动作、参数表和工作台面板。27 个领域节点的数量来自主页与 Xaihi README；此图是架构示意，不代表界面截图或新的实机验证结论。",b,INK,"en" if en else "zh-CN")


def damophus(en=False):
    b=[txt(32,49,"SIYUAN QUESTION BANK",18,"#782955",700,mono=True),
       txt(30,101,"siyuan-damophus",40,PLUM,800,maxw=516),
       txt(32,141,"Scan. Index. Practice. Resume." if en else "扫描、索引、练习、恢复。",25,PLUM,600,maxw=516)]
    b += [rect(72,180,286,175,"#ef8cbd",28),rect(56,191,286,175,"#ffafd4",28)]
    quiz=[rect(0,0,286,175,"#fff7fa",24),txt(22,41,"Q",34,PLUM,800),
          line(65,28,252,28,"#d59bb8",7),line(65,49,216,49,"#d59bb8",7),
          rect(20,77,246,35,"#ffd8e7",12),txt(35,102,"A",19,"#782955",700,mono=True),
          line(63,94,233,94,"#d59bb8",5),
          rect(20,122,246,35,LIME,12),txt(35,147,"B",19,FOREST,700,mono=True),
          line(63,139,208,139,"#7c9a51",5),tick(244,139,20,FOREST,3)]
    b += [group(quiz,"translate(40 183) rotate(-5 143 87)")]
    steps=[("scan","扫描"),("index","索引"),("practice","练习"),("resume","恢复")]
    b += [line(402,197,402,333,"#d59bb8",3)]
    for i,(english,chinese) in enumerate(steps):
        cy=197+i*45
        b += [f'<circle cx="402" cy="{cy}" r="14" fill="{FOREST if i==2 else "#f8bddd"}"/>',
              tick(402,cy,16,LIME,2.5) if i==2 else txt(402,cy+6,str(i+1),16,"#782955",700,mono=True,anchor="middle"),
              txt(426,cy+7,english if en else chinese,21,PLUM,700 if i==2 else 500,maxw=120)]
    b += [txt(32,397,"Practice you can resume." if en else "做到哪，就从哪继续。",24,PLUM,750,maxw=516),
          txt(32,427,"TypeScript · Svelte · SiYuan",18,"#782955",600,maxw=516)]
    return doc(580,448,"siyuan-damophus — a question bank you can resume" if en else "siyuan-damophus：做到哪，就从哪继续",
        "Conceptual practice card, with unlabelled answer placeholders and a four-stage scan/index/practice/resume rail. The SiYuan plugin maintains question indexes and recoverable practice sessions. A/B are interface placeholders, not a real question or answer." if en else
        "练习卡机制示意，以空白选项和扫描、索引、练习、恢复四步侧栏表现思源题库插件的可恢复练习流程。A/B 只是界面占位，不构成真实题目或答案。",b,PALE_ROSE,"en" if en else "zh-CN")


def rossi(en=False):
    bg="#291524"
    b=[txt(32,49,"READER + JS SOURCES",18,ROSE,700,mono=True),
       txt(30,103,"rossi",50,WHITE,800),
       txt(32,143,"One source. One JS file." if en else "每个图源，一个 JS 文件。",25,WHITE,600,maxw=516),
       line(182,261,242,261,ROSE,5),line(354,261,410,261,ROSE,5)]
    source=[rect(0,0,155,177,"#ffd8e7",20),txt(17,35,"source.js",18,PLUM,750,mono=True),
            line(17,54,137,54,"#ef8cbd",3),txt(17,88,"list",23,PLUM,650,mono=True),
            txt(17,120,"search",23,PLUM,650,mono=True),txt(17,152,"images",23,PLUM,650,mono=True)]
    b += [group(source,"translate(35 183) rotate(-4 77 89)"),
          shape("clover4Leaf",298,257,137,LILAC,8),
          txt(298,274,"JS",47,"#282259",850,mono=True,anchor="middle"),
          txt(298,356,"QuickJS",21,ROSE,700,anchor="middle")]
    reader=[rect(0,0,128,174,"#3d2842",24),rect(12,12,104,150,"#fef7ff",14),
            rect(21,21,86,61,LILAC,8),shape("arch",57,58,49,"#454078",-15),
            rect(21,92,38,57,LIME,7),rect(66,92,41,57,ROSE,7),
            line(54,22,54,80,"#fef7ff",3)]
    b += [group(reader,"translate(410 184) rotate(5 64 87)"),
          txt(32,397,"Sources run in a Rust sandbox." if en else "图源逻辑交给 Rust 沙箱执行。",23,WHITE,600,maxw=516),
          txt(32,426,"Flutter · Rust · JS plugin ABI",18,ROSE,600,maxw=516)]
    return doc(580,448,"rossi — one source, one JS file" if en else "rossi：每个图源，一个 JS 文件",
        "Conceptual mechanism: a JS source file describing listing, search and images runs in Rust-side QuickJS, then supplies the Flutter reader. The three labels describe capabilities, not literal ABI entry-point names. The reader artwork contains no third-party comic content." if en else
        "图源机制示意：描述列表、搜索与取图的 JS 文件，经 Rust 侧 QuickJS 执行，交给 Flutter 阅读器展示。list/search/images 是能力标签，不作为字面的 ABI 函数名；阅读器内为抽象图形，没有第三方漫画内容。",b,bg,"en" if en else "zh-CN")


def arcthumbx(en=False):
    ink="#2e1500"
    b=[txt(32,49,"NATIVE COVER THUMBNAILS",18,"#6d3900",700,mono=True),
       txt(30,103,"ArcThumbX",46,ink,800,maxw=516),
       txt(32,142,"Covers, right in your file manager." if en else "封面，直接出现在文件管理器。",24,ink,600,maxw=516),
       rect(32,174,516,201,"#fff5eb",28),
       txt(54,210,"Finder / Explorer",21,"#6d3900",650)]
    for i,(cx,fill,dark,label) in enumerate([(94,LILAC,"#454078","book.epub"),
                                            (271,ORANGE,"#6d3900","vol.cbz"),
                                            (448,BLUE,"#004a75","book.azw3")]):
        x=cx-40
        b += [rect(x,227,98,109,fill,16),
              shape(("arch","fan","gem")[i],x+49,279,73,dark,(-8,8,0)[i]),
              line(x+18,318,x+79,318,"#fff5eb",4),
              txt(x+49,358,label,16,"#6d3900",650,mono=True,anchor="middle")]
    b += [txt(32,401,"CBZ · CBR · EPUB · FB2 · AZW3",18,"#6d3900",650,maxw=516),
          txt(32,430,"Rust · Slint",18,"#6d3900",600)]
    return doc(580,448,"ArcThumbX — covers in Finder and Explorer" if en else "ArcThumbX：封面，直接出现在文件管理器",
        "Conceptual Finder/Explorer window with three cover thumbnails and example file names. Native archive and ebook thumbnail integration, including CBZ, CBR, EPUB, FB2 and AZW3. Covers are original abstract illustrations." if en else
        "原生文件管理器机制示意：Finder / Explorer 中展示三张抽象封面和示例文件名。压缩包与电子书封面缩略图集成，列举 CBZ、CBR、EPUB、FB2、AZW3；封面为原创抽象图形。",b,PEACH,"en" if en else "zh-CN")


def xlchemy(en=False):
    bg="#282259"
    b=[txt(32,49,"BATCH IMAGE CONVERSION",18,ORANGE,700,mono=True),
       txt(30,103,"Xlchemy",50,WHITE,800),
       txt(32,142,"Batch conversion. Native Mac builds." if en else "图片批量转码，原生包直接用。",24,WHITE,600,maxw=516)]
    for x,y,fill,rot in [(60,188,"#7b7091",-12),(46,203,LILAC,-7),(32,219,"#fef7ff",-2)]:
        photo=[rect(0,0,126,127,fill,19),rect(12,12,102,80,"#b5afef",10),
               '<path d="M12 92l35-49 29 29 18-17 20 37Z" fill="#454078"/>',
               line(17,110,99,110,"#454078",5)]
        b += [group(photo,f"translate({x} {y}) rotate({rot} 63 63)")]
    b += [wave(172,266,48,LILAC,4,30,4),
          shape("softBurst",289,260,139,ORANGE,8),
          txt(289,280,"X",59,"#2e1500",850,anchor="middle"),
          line(359,262,389,262,LILAC,4),
          '<path d="M381 252l12 10-12 10" fill="none" stroke="#c3bdfe" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>']
    for y,label,fill,ink in [(185,".jxl",LIME,FOREST),(245,".avif",BLUE,NAVY),(305,".webp",ROSE,PLUM)]:
        b += [rect(407,y,141,46,fill,23),txt(477.5,y+31,label,24,ink,750,mono=True,anchor="middle")]
    b += [txt(32,397,"macOS · Apple Silicon",25,WHITE,750,maxw=516),
          txt(32,426,"Python · packaged encoders",18,LILAC,600,maxw=516)]
    return doc(580,448,"Xlchemy — batch conversion and native Mac builds" if en else "Xlchemy：图片批量转码，原生包直接用",
        "Conceptual batch-conversion illustration: stacked images pass through Xlchemy into JPEG XL, AVIF and WebP. The profile and project README describe native Apple Silicon Mac packages and bundled encoder dependencies. No compression ratio is claimed." if en else
        "批量转码机制示意：图片组经 Xlchemy 转为 JPEG XL、AVIF、WebP。主页与项目 README 记载了 Apple Silicon macOS 原生包及编码器依赖装箱；图中不承诺压缩比例。",b,bg,"en" if en else "zh-CN")


def czkawka(en=False):
    b=[txt(32,49,"DUPLICATE + SIMILAR IMAGES",18,FOREST,700,mono=True),
       txt(30,103,"czkawka-tauri",42,FOREST,800,maxw=516),
       txt(32,142,"Group similar images. Choose a keeper." if en else "重复与相似图片，成组清理。",24,FOREST,600,maxw=516)]
    for x,y,rot,fill in [(47,199,-12,"#e9f5d6"),(120,185,-1,"#f5ffe8"),(206,205,12,"#ffffff")]:
        photo=[rect(0,0,137,139,fill,19),rect(10,10,117,94,"#b5afef",12),
               '<circle cx="96" cy="35" r="12" fill="#e9ddff"/>',
               '<path d="M10 104l38-59 31 40 19-23 29 42Z" fill="#454078"/>',
               line(17,121,102,121,"#7c9a51",5)]
        b += [group(photo,f"translate({x} {y}) rotate({rot} 68 69)")]
    b += [shape("sunny",470,250,102,FOREST,8),tick(470,250,48,LIME,7),
          txt(470,328,"you choose" if en else "自选保留",20,FOREST,700,anchor="middle"),
          txt(32,377,"Windows builds · themes · Taskfile",20,FOREST,600,maxw=516),
          txt(32,426,"Tauri 2 · TypeScript",18,FOREST,650)]
    return doc(580,448,"czkawka-tauri — group similar images and choose a keeper" if en else "czkawka-tauri：重复与相似图片，成组清理",
        "Conceptual group of similar landscape images with a user-selected keeper. The fork's profile description records Windows builds, custom themes and a Taskfile task set. The drawing does not represent an automatic deletion result or a measured similarity score." if en else
        "相似图片分组机制示意：一组相似风景图，由用户自选保留项。该分支在主页中的描述包含 Windows 构建、自定义主题与 Taskfile 任务集；不表示自动删除结果或实测相似度。",b,LIME,"en" if en else "zh-CN")


def hibernal(en=False):
    bg="#10282f"
    b=[txt(32,49,"MACOS MENU BAR",18,BLUE,700,mono=True),
       txt(30,103,"hibernal",50,WHITE,800),
       txt(32,142,"Deep hibernation from the menu bar." if en else "从菜单栏，进入深度休眠。",24,WHITE,600,maxw=516),
       rect(32,178,278,174,"#cde5ff",28),
       txt(53,212,"hibernal",20,NAVY,750),
       line(49,229,293,229,"#95bcdc",2),rect(47,243,248,47,LIME,23.5),
       txt(171,274,"Deep hibernate" if en else "立即休眠",23,FOREST,750,anchor="middle"),
       txt(53,326,"pmset + helper",19,"#004a75",650,mono=True),
       '<circle cx="440" cy="249" r="77" fill="#c3bdfe"/>',
       f'<circle cx="475" cy="220" r="66" fill="{bg}"/>',
       shape("sunny",377,185,24,BLUE,8),shape("softBurst",524,310,25,LIME,10),
       txt(482,341,"Z",49,BLUE,850),
       txt(32,398,"Swift · privileged helper",23,WHITE,650,maxw=516),
       txt(32,428,"On-demand deep hibernation" if en else "按需触发的 macOS 系统工具",20,BLUE,550,maxw=516)]
    return doc(580,448,"hibernal — deep hibernation from the menu bar" if en else "hibernal：从菜单栏，进入深度休眠",
        "Conceptual macOS menu excerpt with a Deep hibernate action, plus a crescent moon. A Swift menu-bar tool invokes pmset through a privileged helper. The illustration describes the trigger and mechanism, not a guarantee that every device successfully hibernates." if en else
        "菜单栏机制示意：立即休眠操作、pmset 与特权 helper，配以月牙图形。Swift 编写的 macOS 菜单栏工具，图中表现触发方式与实现机制，不作为每台设备必然成功休眠的承诺。",b,bg,"en" if en else "zh-CN")


def section_work(en=False):
    return doc(1200,104,"Selected work" if en else "代表作品",
        "Each project is a separate linked SVG, arranged by the surrounding HTML." if en else "每个项目是一张独立 SVG，由外层 HTML 排列并链接到各自仓库。",
        [shape("sunny",49,52,48,LIME,12),txt(92,68,"Selected work" if en else "代表作品",40,WHITE,750),
         txt(1155,62,"TOOLS I USE MYSELF" if en else "做给自己用的工具",20,MUTED,600,anchor="end")],INK,"en" if en else "zh-CN",28)


def section(en, name, chinese, english, note_zh, note_en, motif, accent):
    return doc(1200,104,english if en else chinese,
        ("Profile section: " + english) if en else ("个人主页章节：" + chinese),
        [shape(motif,49,52,48,accent,12),txt(92,68,english if en else chinese,40,WHITE,750),
         txt(1155,62,note_en if en else note_zh,20,MUTED,600,anchor="end",maxw=650)],INK,"en" if en else "zh-CN",28)


def section_domain(en=False):
    return section(en,"domain","领域索引","By domain","本地工具与底层机制","LOCAL TOOLS & THEIR INNER WORKINGS","clover4Leaf",BLUE)


def section_law(en=False):
    return section(en,"law","法律 × AI","Law × AI","来源能回查，产物过门禁","TRACEABLE SOURCES · CHECKED OUTPUTS","arch",ROSE)


def section_method(en=False):
    return section(en,"method","我怎么做事","How I work","模块化 · 中文正确性 · 本地优先","MODULAR · CJK-CORRECT · LOCAL-FIRST","softBurst",ORANGE)


# One registry keeps generation, gallery links, alt text and preview order aligned.
PROJECTS = [
    ("MineruCustom","minerucustom",mineru,"MinerU 后处理：捡回脚注，找回原页。","Restore footnotes and page marks after MinerU."),
    ("skilloom","skilloom",skilloom,"Agent 技能包与门禁：产物不合格，就拒收。","Agent skills and gates that reject invalid output."),
    ("neoview","neoview",neoview,"本地图像与漫画阅读器，以 Rust + SQLite 维护缩略图和目录缓存。","Local image and manga reader with Rust + SQLite caching."),
    ("grzeb","grzeb",grzeb,"目录级全文检索，按结果树下钻，解码正文缓存进 SQLDelight。","Directory search with a navigable result tree and SQLDelight text cache."),
    ("Xaihi","xaihi",xaihi,"27 个领域节点以插件包接入 DeepSeek Harness，包含动作、参数和面板。","27 domain nodes plug actions, schemas and panels into DeepSeek Harness."),
    ("siyuan-damophus","damophus",damophus,"思源题库插件：扫描、索引、练习、恢复。","SiYuan question-bank plugin: scan, index, practice and resume."),
    ("rossi","rossi",rossi,"每个图源是一个 JS 文件，由 Rust 侧 QuickJS 执行并交给 Flutter 阅读器。","JS source plugins run in Rust-side QuickJS and feed a Flutter reader."),
    ("ArcThumbX","arcthumbx",arcthumbx,"在 Finder 与资源管理器中直接展示压缩包与电子书封面。","Native archive and ebook cover thumbnails in Finder and Explorer."),
    ("Xlchemy","xlchemy",xlchemy,"批量转 JPEG XL、AVIF、WebP，提供 Apple Silicon macOS 原生包。","Batch JPEG XL, AVIF and WebP conversion, with native Apple Silicon Mac builds."),
    ("czkawka-tauri","czkawka-tauri",czkawka,"重复与相似图片分组清理，自出 Windows 构建并加入主题和 Taskfile。","Duplicate and similar-image cleanup with Windows builds, themes and Taskfile tasks."),
    ("hibernal","hibernal",hibernal,"Swift 菜单栏工具，通过 pmset 与特权 helper 按需深度休眠。","Swift menu-bar tool for deep hibernation via pmset and a privileged helper."),
]


def gallery(en=False):
    suffix=".en" if en else ""
    rows=["<!-- Each project is a separate SVG; only this HTML arranges the cards. -->"]
    for i in range(0,len(PROJECTS),2):
        rows += ['<p align="center">']
        for repo,slug,_,zh,english in PROJECTS[i:i+2]:
            alt=repo+(": " if en else "：")+(english if en else zh)
            rows += [f'  <a href="https://github.com/HibernalGlow/{repo}"><img src="./assets/readme/proj-{slug}{suffix}.svg" width="400" alt="{escape(alt,quote=True)}"></a>']
        rows += ["</p>",""]
    return "\n".join(rows)


def embed():
    root=OUT.parent.parent
    marker="<!-- Each project is a separate SVG; only this HTML arranges the cards. -->"
    for en in (False,True):
        path=root/("README.en.md" if en else "README.md")
        text=path.read_text(encoding="utf-8")
        start=text.index(marker)
        end=text.index("| Project | Stack | What it is |" if en else "| 项目 | 技术栈 | 是什么 |",start)
        text=text[:start]+gallery(en)+"\n"+text[end:]
        if en:
            for key in ("domain","law","method"):
                text=text.replace(f'./assets/readme/section-{key}.svg',f'./assets/readme/section-{key}.en.svg')
        path.write_text(text,encoding="utf-8")


if __name__ == "__main__":
    renderers=[("hero",hero)]+[("proj-"+slug,render) for _,slug,render,_,_ in PROJECTS]+[
        ("section-work",section_work),("section-domain",section_domain),
        ("section-law",section_law),("section-method",section_method)]
    for filename,render in renderers:
        for en in (False,True):
            path=OUT / (filename + (".en" if en else "") + ".svg")
            path.write_text(render(en),encoding="utf-8")
            print(path.relative_to(OUT))
    if "--embed" in sys.argv:
        embed()
