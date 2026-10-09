import unittest,json,sys
from pathlib import Path
from html.parser import HTMLParser
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from build import ROOT,render
class Links(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  for k in ('src','href'):
   if a.get(k):self.refs.append(a[k])
class SiteTests(unittest.TestCase):
 def test_publications_are_unique_and_authored(self):
  ps=json.loads((ROOT/'data/publications.json').read_text())['publications'];self.assertEqual(len(ps),9);self.assertEqual(len({p['id'] for p in ps}),9)
  for p in ps:self.assertIn('Yifan Zhu',p['authors']);self.assertTrue(p['links']);self.assertTrue(all(l['url'].startswith('https://') for l in p['links']))
 def test_seed_metadata_and_author_position(self):
  ps={p['id']:p for p in json.loads((ROOT/'data/publications.json').read_text())['publications']}
  self.assertTrue(ps['seed3d-1']['title'].startswith('Seed3D 1.0:'));self.assertNotEqual(ps['seed3d-1']['authors'][0],'Yifan Zhu');self.assertEqual(ps['seed3d-2']['year'],2026)
 def test_assets_and_anchors_exist(self):
  parser=Links();parser.feed(render())
  for ref in parser.refs:
   if ref.startswith('#') and len(ref)>1:self.assertIn(ref[1:],parser.ids)
   elif not ref.startswith(('https://','mailto:','#')):self.assertTrue((ROOT/ref).is_file(),ref)
 def test_compact_homepage_content(self):
  s=render();self.assertEqual(s.count('<article '),6)
  self.assertLess(s.index("master's degree"),s.index('Selected research'))
  self.assertIn('I work on 3D generation at ByteDance.',s)
  for phrase in ('From understanding the world','EARLIER &amp; ADDITIONAL WORK','My earlier work','<nav','mailto:','Long-Range Outdoor','Manufacturing Defects','Surface Defect Detection'):self.assertNotIn(phrase,s)
  self.assertIn('4og2ymo754zx7.png',s)
 def test_generated_html_is_current(self):self.assertEqual((ROOT/'index.html').read_text(),render())
 def test_no_fake_video_or_template_identity(self):
  s=render();self.assertNotIn('<video',s);self.assertNotIn('jonbarron.info',s);self.assertNotIn('seed3d1_0_stop',s);self.assertNotIn('{{',s)
if __name__=='__main__':unittest.main()
