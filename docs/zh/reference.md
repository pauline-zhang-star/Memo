# Memo — 跨平台、跨设备内容存储与检索 skill

规范页面：https://pauline-zhang-star.github.io/Memo/zh/
项目源码：https://github.com/pauline-zhang-star/Memo

Memo 是免费的 AI skill，用于跨 ChatGPT、Claude、Gemini，以及支持的电脑、手机和平板，存储和查找讨论摘要。内容以 Google Docs 保存在自己的 Google Drive 中。输入 /memo 保存，输入 /memo 加主题词搜索并读取。每个平台和设备都需要提供 Memo 及相应的 Drive 能力。

## 基本事实
- 适配平台: ChatGPT, Claude, Gemini
- 适用设备: 支持相应能力的电脑、手机和平板
- 存储位置: 自己的 Google Drive；原生 Google Docs
- Skill 价格: 免费；可选安装器单独收费
- 所需能力: Drive 搜索和读取；保存还需写入或导出
- 规则版本: 0.4.18

## 在一台设备保存， 在另一台设备找回。
/memo — Memo 总结当前上下文，写入 Drive，读回正文并检查存放位置。回复必须如实说明实际完成的核验。
/memo topic — Memo 搜索相关记录、读取正文，返回关键决定、未决问题与来源链接。主题是检索关键词，不要求与文档标题完全一致。

## 选择你使用的平台。

### ChatGPT
1. 打开 Memo 仓库。插件目录结构包括 plugin.json、assets/ 和 skills/memo/SKILL.md。
2. 导入插件时，将 ChatGPT 专用规则放到 skills/memo/SKILL.md，与 plugin.json、assets/ 一起打包，再通过账号实际提供的插件上传入口导入。
3. 安装或启用 Memo，在对话中选中它。连接 Google Drive 应用，分别检查所需工具是否可用。
https://github.com/pauline-zhang-star/Memo/blob/main/platforms/chatgpt/memo/SKILL.md

### Claude
1. 打开 Claude 专用规则文件，通过 GitHub 原始文件下载保存为 SKILL.md。
2. 在 Claude 自定义设置中打开 Skills，通过当前界面接受的格式上传技能，导入后启用 Memo。
3. 在 Claude 连接 Google Drive；在支持的对话中选择或调用 Memo，分别检查搜索、读取与写入能力。
https://github.com/pauline-zhang-star/Memo/blob/main/platforms/claude/memo/SKILL.md

### Gemini
1. 打开 Gemini 专用规则文件，保存 SKILL.md。
2. 在 Gemini 打开“自定义 → 技能”，通过实际提供的上传或创建入口导入。若手动填写指令，使用 YAML 元数据之后的规则正文，技能命名为 memo。
3. 保存并启用技能，连接可用的 Google Workspace／Drive 集成；检索时明确要求 Memo 在 Google Drive 中查找。
https://github.com/pauline-zhang-star/Memo/blob/main/platforms/gemini/memo/SKILL.md

## 一个共享文件夹， 串联不同平台与设备。
首次使用默认在“我的云端硬盘”根目录创建或复用 Memo 文件夹。各平台使用同一 Google 账号和文件夹，或一个已经明确共享、各平台均可访问的文件夹。

## FAQ

### 当前对话找不到 Memo
确认当前平台和模式下已安装、启用并选中 Memo。网页、手机、Chat 和 Work 的可用入口可能不同。只输入 /memo 不会自动完成安装。

### 保存出来的文档是空白
创建文件与写入正文是不同操作。Memo 应按返回的文档 ID 直接读取，必要时在同一文档补写一次，而不是重复创建空文件。请以实际核验结果为准。

### 搜索没有找到已有 Memo
尝试主题别名和中英文关键词。优先使用实际提供的 Drive 文件搜索；普通 Workspace 上下文搜索可能漏掉刚修改的文件。直接提供文档链接，有助于区分搜索失败和文件不存在。

### 为什么又出现权限提示？
各平台独立控制 Drive 授权和单次工具操作确认。已有授权可用时应复用，但 Memo 无法取消必要的确认，也不能自行获得永久权限。

### Memo 会自动读取其他聊天吗？
不会。仅保存当前可见或明确提供的上下文。检索读取相关的 Drive 摘要，并非浏览 AI 账号里的全部聊天。

## 不想手动配置？
也可以购买单独的 Memo Setup 自动安装器，省去逐个平台配置 skill 的步骤。登录和授权仍需自行完成。当前安装器适用于 macOS 13+、Apple Silicon 和 Chrome。
安装器商品上架后，这里会补充购买链接。免费 skill 可独立使用。

文档核对日期：2026 年 11 月 1 日。平台能力与菜单可能变化。
独立项目，与 OpenAI、Anthropic 或 Google 无官方关联。
