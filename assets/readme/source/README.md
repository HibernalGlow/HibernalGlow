# SVG 源文件

已重写全部 11 个代表项目、独立 hero 和四个章节标题。中英文分别输出；每个项目对应一个完整 SVG，项目之间的布局只存在于 README 的 HTML 中。每张项目卡使用 `580 × 448` 画布，HTML 以 400 CSS 像素宽度并排展示，窄屏由 GitHub 的图片最大宽度规则自然换行。

```sh
python3 assets/readme/source/build.py
# 同时更新 README 中的项目网格和英文章节图路径；正文及项目表不变
python3 assets/readme/source/build.py --embed
```

文案依据主页 README，以及 MineruCustom、skilloom、grzeb、Xaihi、siyuan-damophus、rossi、ArcThumbX、Xlchemy、hibernal 的本地项目 README。czkawka-tauri 的描述仅沿用主页已列出的功能。页码 42 与 E411 / E625 来自项目原有示例，Xaihi 的 27 个节点与主页及项目文档一致。缩略图、目录树示例路径、练习卡和文件图形为机制示意，并非产品截图或实测结果；未引入额外 Star 数、提交数、相似度、压缩率或性能数据。

| 项目 | 构图重点 |
| --- | --- |
| MineruCustom | 脚注与页码恢复前后对照 |
| skilloom | 真实拒收示例与非零退出码 |
| neoview | 缩略图生成与本地缓存 |
| grzeb | 可钻取的目录结果树 |
| Xaihi | 宿主与动作、参数、面板插件包 |
| siyuan-damophus | 可恢复练习卡与四步侧栏 |
| rossi | JS 图源、QuickJS、阅读器 |
| ArcThumbX | 原生文件管理器里的封面 |
| Xlchemy | 成组图片转为三种图像格式 |
| czkawka-tauri | 相似图分组与自选保留 |
| hibernal | 菜单栏操作与休眠月牙 |

设计采用 Material 3 Expressive 的强调字重、形状对比、连接按钮组和波浪进度元素。画布尺寸、构图与间距是本项目的插画设计选择，不作为 Material 组件的 dp 规格。配色沿用本次草稿中由 Material Color Utilities 0.4.0、2025 spec、SchemeExpressive、种子 `#5d50c8` 生成的静态角色色，补色取自已协调的蓝色、橙色家族。

`expressive-shapes.json` 仅保留所用的九种轮廓，来自 `material_new_shapes` 1.0.0 导出的三次贝塞尔数据。该包是第三方移植；许可见同目录 `material-shapes-LICENSE.txt`。SVG 不加载字体、脚本或外部图像。
