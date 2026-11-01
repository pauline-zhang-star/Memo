"""Render crawlable bilingual documentation and matching discovery metadata."""
from pathlib import Path
from html import escape, unescape
from html.parser import HTMLParser
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs'
BASE = 'https://pauline-zhang-star.github.io/Memo/'
REPO = 'https://github.com/pauline-zhang-star/Memo'
SOURCE = (ROOT / 'site-src/index.template.html').read_text()
ZH = json.loads((ROOT / 'site-src/zh.json').read_text())
TRANSLATABLE = re.compile(r'<([a-z][\w-]*)(\b[^>]*\bdata-t="([^"]+)"[^>]*)>(.*?)</\1>', re.S)
EN = {match[3]:match[4] for match in TRANSLATABLE.finditer(SOURCE)}
assert set(EN) <= set(ZH), set(EN)-set(ZH)


def plain(text):
    return unescape(re.sub(r'<[^>]+>', ' ', text)).strip()


def text_reference(lang, data):
    zh = lang == 'zh-CN'
    lines = ['# Memo — '+('跨平台、跨设备内容存储与检索 skill' if zh else 'Cross-platform, cross-device memory storage and retrieval skill'), '',
             ('规范页面：' if zh else 'Canonical page: ')+BASE+('zh/' if zh else ''),
             ('项目源码：' if zh else 'Project source: ')+REPO, '', plain(data['quickAnswer']), '',
             '## '+('基本事实' if zh else 'Facts'),
             '- '+plain(data['factPlatforms'])+': ChatGPT, Claude, Gemini',
             '- '+plain(data['factDevices'])+': '+plain(data['factDevicesValue']),
             '- '+plain(data['factStorage'])+': '+plain(data['factStorageValue']),
             '- '+plain(data['factCost'])+': '+plain(data['factCostValue']),
             '- '+plain(data['factRequirements'])+': '+plain(data['factRequirementsValue']),
             '- '+plain(data['factVersion'])+': 0.4.18', '',
             '## '+plain(data['usageTitle']), '/memo — '+plain(data['saveBody']),
             '/memo topic — '+plain(data['recallBody']), '', '## '+plain(data['installTitle'])]
    for platform, keys in [('ChatGPT',['gpt1','gpt2','gpt3']),('Claude',['claude1','claude2','claude3']),('Gemini',['gemini1','gemini2','gemini3'])]:
        lines += ['', '### '+platform]
        lines += [str(i+1)+'. '+plain(data[key]) for i,key in enumerate(keys)]
        lines += [REPO+'/blob/main/platforms/'+platform.lower()+'/memo/SKILL.md']
    lines += ['', '## '+plain(data['driveTitle']),plain(data['driveText']), '', '## FAQ']
    for i in range(1,6): lines += ['', '### '+plain(data['q'+str(i)]),plain(data['a'+str(i)])]
    lines += ['', '## '+plain(data['optionalTitle']),plain(data['optionalText']),plain(data['purchasePending']), '',plain(data['reviewed']),plain(data['footer']), '']
    return '\n'.join(lines)


def render(lang):
    zh = lang == 'zh-CN'
    data = ZH if zh else EN
    url = BASE+('zh/' if zh else '')
    title = 'Memo — 跨平台、跨设备保存与查找 | ChatGPT、Claude、Gemini' if zh else 'Memo — Cross-Platform, Cross-Device Memory for ChatGPT, Claude & Gemini'
    description = ('免费 Memo skill：跨 ChatGPT、Claude、Gemini 保存和查找内容，通过自己的 Google Drive 在支持的电脑、手机和平板间找回讨论摘要。含三平台手动安装说明。' if zh else 'Free Memo skill: save and find discussion summaries across ChatGPT, Claude and Gemini, on supported computers, phones and tablets through your own Google Drive. Manual setup guides included.')
    page = TRANSLATABLE.sub(lambda m:'<'+m[1]+m[2]+'>'+ZH[m[3]]+'</'+m[1]+'>', SOURCE) if zh else SOURCE
    page = page.replace('<html lang="en">','<html lang="'+lang+'">')
    page = re.sub(r'<a id="language"[^>]+>.*?</a>', '<a id="language" href="'+('../' if zh else './zh/')+'" lang="'+('en' if zh else 'zh-CN')+'" hreflang="'+('en' if zh else 'zh-CN')+'">'+('English' if zh else '中文')+'</a>',page)
    schema = {'@context':'https://schema.org','@graph':[
        {'@type':'WebSite','@id':BASE+'#website','name':'Memo','url':BASE,'inLanguage':['en','zh-CN']},
        {'@type':'WebPage','@id':url+'#webpage','url':url,'name':title,'description':description,'inLanguage':lang,'isPartOf':{'@id':BASE+'#website'},'about':{'@id':BASE+'#skill'},'dateModified':'2026-11-01','mainEntity':{'@id':url+'#faq'}},
        {'@type':'SoftwareSourceCode','@id':BASE+'#skill','name':'Memo','alternateName':'Memo skill','description':plain(data['quickAnswer']),'url':BASE,'codeRepository':REPO,'version':'0.4.18','runtimePlatform':['ChatGPT','Claude','Gemini'],'author':{'@type':'Person','name':'pauline-zhang-star','url':'https://github.com/pauline-zhang-star'},'subjectOf':{'@id':url+'#webpage'}},
        {'@type':'FAQPage','@id':url+'#faq','inLanguage':lang,'mainEntity':[{'@type':'Question','name':plain(data['q'+str(i)]),'acceptedAnswer':{'@type':'Answer','text':plain(data['a'+str(i)])}} for i in range(1,6)]}
    ]}
    prefix = '../' if zh else './'
    head = '<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
    head += '<title>'+escape(title)+'</title>\n<meta name="description" content="'+escape(description,quote=True)+'">\n'
    head += '<meta name="theme-color" content="#e5f3f8">\n<meta name="robots" content="index,follow,max-image-preview:large">\n'
    head += '<link rel="canonical" href="'+url+'">\n'
    for hreflang, location in [('en',BASE),('zh-CN',BASE+'zh/'),('x-default',BASE)]: head += '<link rel="alternate" hreflang="'+hreflang+'" href="'+location+'">\n'
    head += '<link rel="sitemap" type="application/xml" href="'+BASE+'sitemap.xml">\n'
    for key,value in [('og:type','website'),('og:site_name','Memo'),('og:title',title),('og:description',description),('og:url',url),('og:locale','zh_CN' if zh else 'en_US'),('og:image',BASE+'assets/memo-icon.png'),('og:image:alt','Memo skill icon'),('og:image:width','1024'),('og:image:height','1024')]: head += '<meta property="'+key+'" content="'+escape(value,quote=True)+'">\n'
    for key,value in [('twitter:card','summary'),('twitter:title',title),('twitter:description',description),('twitter:image',BASE+'assets/memo-icon.png')]: head += '<meta name="'+key+'" content="'+escape(value,quote=True)+'">\n'
    head += '<link rel="icon" href="'+prefix+'assets/memo-icon.png">\n<link rel="stylesheet" href="'+prefix+'base.css">\n<link rel="stylesheet" href="'+prefix+'docs.css">\n<script defer src="'+prefix+'docs.js"></script>\n'
    head += '<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('<','\\u003c')+'</script>\n</head>'
    page = re.sub(r'<head>.*?</head>',lambda _:head,page,flags=re.S)
    if zh:
        page=page.replace('src="./assets/','src="../assets/').replace('href="./sitemap.xml"','href="../sitemap.xml"')
    folder = OUT/'zh' if zh else OUT
    folder.mkdir(exist_ok=True)
    (folder/'index.html').write_text(page)
    (folder/'reference.md').write_text(text_reference(lang,data))


for language in ['en','zh-CN']: render(language)
(OUT/'sitemap.xml').write_text('''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
'''+''.join('<url><loc>'+url+'</loc><lastmod>2026-11-01</lastmod><xhtml:link rel="alternate" hreflang="en" href="'+BASE+'"/><xhtml:link rel="alternate" hreflang="zh-CN" href="'+BASE+'zh/"/></url>\n' for url in [BASE,BASE+'zh/'])+'</urlset>\n')
(OUT/'llms.txt').write_text('''# Memo

> Free skill for storing and finding discussion summaries across ChatGPT, Claude and Gemini, on supported computers, phones and tablets. Records live in the user's Google Drive as Google Docs. The same accessible folder and required platform tools are needed.

## Documentation
- [English documentation]('''+BASE+'''): What Memo does, save/retrieve commands, platform-specific manual setup, permissions and troubleshooting.
- [中文说明]('''+BASE+'''zh/): 产品定义、保存与检索、三平台手动安装、Drive 权限和问题排查。
- [English text reference]('''+BASE+'''reference.md): Same project facts in Markdown.
- [中文纯文本说明]('''+BASE+'''zh/reference.md): 相同事实的 Markdown 版本。
- [Project source]('''+REPO+'''): Public skill instructions; excludes the paid installer and personal configuration.

## Optional installer
Memo Setup is a separate paid convenience tool for supported Macs, not a requirement for using the free skill. No installer binary or purchase link is published here yet.
''')
print('Rendered English/Chinese HTML, matching metadata and FAQ schema, sitemap and text references.')
