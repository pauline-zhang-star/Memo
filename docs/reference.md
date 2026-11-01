# Memo — Cross-platform AI conversation memory skill

Canonical page: https://pauline-zhang-star.github.io/Memo/
Project source: https://github.com/pauline-zhang-star/Memo

Memo is a free, independently developed AI skill that saves concise discussion summaries as Google Docs in your own Google Drive. Use /memo to save the visible discussion, or /memo followed by a topic to search and read previous summaries. Each platform must provide the required Drive tools.

## Facts
- Platforms: ChatGPT, Claude, Gemini
- Storage: Your Google Drive; native Google Docs
- Skill price: Free; the optional installer is separate
- Requirements: Drive search/read; writing or export for saving
- Rule version: 0.4.18

## Save now. Recall later.
/memo — Memo summarizes the current context, writes it to Drive, reads back the body and checks its destination. It must report what was actually verified.
/memo topic — Memo searches relevant records, reads their content and returns key decisions, open questions and source links. A topic is a search keyword, not an exact document title.

## Choose your platform.

### ChatGPT
1. Open the Memo repository. The plugin layout uses plugin.json, assets/ and skills/memo/SKILL.md.
2. For a plugin import, put the ChatGPT-specific rule file at skills/memo/SKILL.md and package it with plugin.json and assets/. Use the plugin upload interface available in your account.
3. Install or enable Memo, then select it in your conversation. Connect the Google Drive app and check that the required tools are available.
https://github.com/pauline-zhang-star/Memo/blob/main/platforms/chatgpt/memo/SKILL.md

### Claude
1. Open the Claude-specific rule file and save it as SKILL.md using GitHub's raw-file download.
2. In Claude's customization settings, open Skills and upload the skill in the format accepted by the current interface. Enable Memo after import.
3. Connect Google Drive in Claude. Select or invoke Memo in a supported conversation and check search, read and write capabilities separately.
https://github.com/pauline-zhang-star/Memo/blob/main/platforms/claude/memo/SKILL.md

### Gemini
1. Open the Gemini-specific rule file and save SKILL.md.
2. In Gemini, open customization → Skills and use the available upload or creation flow. If entering instructions manually, use the rule body after the YAML metadata, and name the skill memo.
3. Save and enable the skill. Connect the available Google Workspace/Drive integration and explicitly ask Memo to search Google Drive when retrieving.
https://github.com/pauline-zhang-star/Memo/blob/main/platforms/gemini/memo/SKILL.md

## One Memo folder. A clear source of truth.
On first use, Memo defaults to creating or reusing a folder named Memo in My Drive root. Use the same Google account and folder across platforms, or an explicitly shared folder each platform can access.

## FAQ

### Memo isn't available in this conversation
Confirm the skill is installed, enabled and selected in the current platform and mode. Availability can differ across web, mobile, Chat and Work. Typing /memo alone does not install anything.

### A saved file looks empty
Creating a file and writing its body are separate operations. Memo should read the returned document ID directly and repair the same document once if needed, rather than create repeated empty files. Ask for the actual verification result.

### A search didn't find my Memo
Try topic aliases and Chinese/English keywords. Use actual Drive file search where available; a general Workspace context search may miss recently changed files. A direct document link can distinguish search failure from a missing file.

### Why does permission appear again?
Each platform controls its Drive authorization and tool-action confirmations. Reuse existing access when possible, but Memo cannot suppress required approvals or grant itself permanent access.

### Does Memo automatically read all my other chats?
No. Save only context that is visible or explicitly supplied. Retrieval reads relevant saved Drive records, not every conversation in your AI accounts.

## Prefer help with setup?
You can also buy Memo Setup, a separate automatic installer, to avoid configuring each skill manually. Sign-in and authorization still require your participation. The current installer targets macOS 13+, Apple Silicon and Chrome.
The purchase link will be added when the installer listing is available. The free skill is usable independently.

Documentation reviewed: November 1, 2026. Platform capabilities and menus can change.
An independent project. Not affiliated with OpenAI, Anthropic or Google.
