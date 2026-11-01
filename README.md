# Memo

Store and find discussion summaries across ChatGPT, Claude and Gemini, and across supported computers, phones and tablets, through your own Google Drive.
通过自己的 Google Drive，跨 ChatGPT、Claude、Gemini，以及支持的电脑、手机和平板，存储与查找讨论摘要。

Project site / 项目说明网站：[Memo documentation](https://pauline-zhang-star.github.io/Memo/)

## Use / 使用

- `/memo` — summarize and save the currently visible discussion. / 总结并保存当前可见的讨论。
- `/memo topic` — search and read saved summaries about that topic. / 搜索并读取相关主题的摘要。

Select or enable Memo in the platform before invoking it. `/memo` is a text convention; it is not a universally registered native slash command.
使用前需在对应平台选择或启用 Memo；`/memo` 是文本触发约定，不代表各平台都注册了同名原生命令。

## Files / 文件

| Path | Purpose / 用途 |
| --- | --- |
| `skills/memo/SKILL.md` | Shared Chinese and English workflow / 通用中英文规则 |
| `platforms/chatgpt/memo/SKILL.md` | ChatGPT adaptation / ChatGPT 适配 |
| `platforms/claude/memo/SKILL.md` | Claude adaptation / Claude 适配 |
| `platforms/gemini/memo/SKILL.md` | Gemini adaptation / Gemini 适配 |
| `plugin.json` | Memo plugin metadata / 插件元数据 |

Version / 版本：0.4.18.

## Setup / 配置

Use the skill import or configuration interface actually available on your platform. Platform, subscription and mobile capabilities vary. Connect Google Drive on each platform you use; searches require file search/read tools, and saving also requires real document-writing tools. A skill supplies instructions, not missing connector capabilities.
通过平台实际提供的技能导入或配置入口使用对应规则。入口和能力随平台、套餐及手机端支持而变化。各平台需连接 Google Drive；检索需要文件搜索和读取工具，保存还需要真实的文档写入能力。Skill 提供工作规则，不能补足平台缺失的工具。

The default destination is a `Memo` folder in Drive root. Generic rules contain null destination settings. Reuse a verified personal folder configuration when supported; never put private account details, tokens, or personal folder IDs into this repository. Saving succeeds only after the document body is read back and its location is verified.
默认在 Drive 根目录创建或复用 `Memo` 文件夹。通用规则的存储配置保留 null；平台支持时复用经过验证的个人文件夹配置。不要向仓库提交个人账号、令牌或文件夹 ID。保存成功必须以正文读回和位置核验为依据。

## Commercial installer / 收费安装器

This repository publishes the Memo skill rules and documentation only. Memo Setup, the commercial automatic installer, is distributed separately. Its binaries, source code, build scripts and personal installation packages are not included here.
本仓库仅发布 Memo skill 规则与说明。Memo Setup 自动安装器作为单独的收费产品分发；此处不包含安装器、安装器源码、构建脚本或个人安装包。

Memo is an independent project, not an official product of OpenAI, Anthropic or Google.
Memo 是独立项目，并非 OpenAI、Anthropic 或 Google 的官方产品。

## Documentation publishing / 文档发布

- English: https://pauline-zhang-star.github.io/Memo/
- 中文：https://pauline-zhang-star.github.io/Memo/zh/
- Source templates: `site-src/`; render both languages with `python3 scripts/build_docs.py`.
- Checks: `python3 -m unittest discover -s tests -v`.
- GitHub Pages publishes `docs/` from `main`. Both language pages contain the full text without requiring JavaScript. JavaScript only enhances tabs and the optional external purchase link.
- The sitemap, matching JSON-LD and text references describe the actual visible content. `llms.txt` is an optional navigation aid, not a search-engine requirement or a guarantee of AI citations. No ranking or indexing claims are made.
- A GitHub project site cannot control the host-level `/robots.txt` from its own `/Memo/` directory. The host-level file was absent (404) and the live page had no `X-Robots-Tag` restriction when checked. No ineffective project-local crawler rules were added.

To measure results, verify the exact site prefix in Google Search Console and Bing Webmaster Tools and submit `https://pauline-zhang-star.github.io/Memo/sitemap.xml`. Those account verifications and submissions have not been performed. Indexing, citations and traffic must be measured after deployment; a passed source check is not proof of visibility in AI answers.
