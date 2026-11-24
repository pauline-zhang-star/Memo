# Documentation publishing / 文档发布

Maintainer notes; not end-user setup instructions. / 维护者工作说明，非用户安装教程。


- English: https://pauline-zhang-star.github.io/Memo/
- 中文：https://pauline-zhang-star.github.io/Memo/zh/
- Source templates: `site-src/`; render both languages with `python3 scripts/build_docs.py`.
- Checks: `python3 -m unittest discover -s tests -v`.
- GitHub Pages publishes `docs/` from `main`. Both language pages contain the full text without requiring JavaScript. JavaScript only enhances tabs and the optional external purchase link.
- The sitemap, matching JSON-LD and text references describe the actual visible content. `llms.txt` is an optional navigation aid, not a search-engine requirement or a guarantee of AI citations. No ranking or indexing claims are made.
- A GitHub project site cannot control the host-level `/robots.txt` from its own `/Memo/` directory. The host-level file was absent (404) and the live page had no `X-Robots-Tag` restriction when checked. No ineffective project-local crawler rules were added.

To measure results, verify the exact site prefix in Google Search Console and Bing Webmaster Tools and submit `https://pauline-zhang-star.github.io/Memo/sitemap.xml`. Those account verifications and submissions have not been performed. Indexing, citations and traffic must be measured after deployment; a passed source check is not proof of visibility in AI answers.
