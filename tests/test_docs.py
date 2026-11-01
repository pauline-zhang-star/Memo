import json
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT/'docs'
BASE = 'https://pauline-zhang-star.github.io/Memo/'

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.tags=[]; self.ids=[]; self.text=[]; self.feed(text)
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs); self.tags.append((tag,attrs))
        if 'id' in attrs:self.ids.append(attrs['id'])
    def handle_data(self,data):self.text.append(data)

class DocumentationTests(unittest.TestCase):
    def test_language_pages_are_complete_without_javascript(self):
        for path,lang in [('index.html','en'),('zh/index.html','zh-CN')]:
            with self.subTest(path=path):
                source=(DOCS/path).read_text(); doc=Document(source)
                self.assertIn(('html',{'lang':lang}),doc.tags)
                definition = re.search(r'<p data-t="quickAnswer">(.*?)</p>',source,re.S)[1]
                self.assertIn('Memo',definition)
                self.assertIn('Google Drive',definition)
                self.assertEqual(len(doc.ids),len(set(doc.ids)))
                panels=[a for tag,a in doc.tags if a.get('role')=='tabpanel']
                self.assertEqual(len(panels),3)
                self.assertTrue(all('hidden' not in a for a in panels))
    def test_canonicals_and_language_alternates(self):
        for path,canonical in [('index.html',BASE),('zh/index.html',BASE+'zh/')]:
            doc=Document((DOCS/path).read_text())
            links=[a for tag,a in doc.tags if tag=='link']
            self.assertEqual([a['href'] for a in links if a.get('rel')=='canonical'],[canonical])
            alternatives={a['hreflang']:a['href'] for a in links if a.get('rel')=='alternate'}
            self.assertEqual(alternatives,{'en':BASE,'zh-CN':BASE+'zh/','x-default':BASE})
    def test_structured_answers_match_visible_answers(self):
        for file in [DOCS/'index.html',DOCS/'zh/index.html']:
            source=file.read_text()
            graph=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',source,re.S)[1])['@graph']
            faq=next(item for item in graph if item['@type']=='FAQPage')
            for i,item in enumerate(faq['mainEntity'],1):
                for key,text in [('q',item['name']),('a',item['acceptedAnswer']['text'])]:
                    visible=re.search(r'<[^>]+data-t="'+key+str(i)+r'"[^>]*>(.*?)</[^>]+>',source,re.S)[1]
                    self.assertEqual(unescape(re.sub('<[^>]+>',' ',visible)).strip(),text)
            self.assertNotIn('aggregateRating',source)
    def test_relative_assets_links_and_fragments_exist(self):
        for file in [DOCS/'index.html',DOCS/'zh/index.html']:
            doc=Document(file.read_text())
            for tag,attrs in doc.tags:
                if tag not in ['a','link','script','img']:continue
                value=attrs.get('href') or attrs.get('src')
                if not value or value.startswith(('https://','http://')):continue
                if value.startswith('#'):
                    if value!='#':self.assertIn(value[1:],doc.ids)
                else:
                    target=(file.parent/value.split('#')[0]).resolve()
                    self.assertTrue(target.exists(),str(target))
                    self.assertTrue(target.is_relative_to(DOCS.resolve()))
    def test_sitemap_and_reference_paths(self):
        tree=ET.parse(DOCS/'sitemap.xml'); ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
        self.assertEqual([x.text for x in tree.findall('s:url/s:loc',ns)],[BASE,BASE+'zh/'])
        for name in ['llms.txt','reference.md','zh/reference.md']:
            text=(DOCS/name).read_text();self.assertIn(BASE,text);self.assertIn('Google Drive',text)
        self.assertIsNone(json.loads((DOCS/'installer-link.json').read_text())['url'])
        self.assertFalse(any(DOCS.rglob('*.zip')))

if __name__=='__main__':unittest.main()
