"""Render the static academic homepage from verified publication metadata."""
import html,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def esc(s):return html.escape(str(s),quote=True)
def authors(items):return ', '.join('<strong>'+esc(a)+'</strong>' if a in ('Yifan Zhu','Yi-Fan Zhu') else esc(a) for a in items)
def author_block(items,core=False):
 if core:return '<details class="team-authors"><summary>Core contributors · alphabetical by last name</summary><p class="authors">'+authors(items)+'</p></details>'
 if len(items)>8:return '<details class="team-authors"><summary>ByteDance Seed team · including Yifan Zhu</summary><p class="authors">'+authors(items)+'</p></details>'
 return '<p class="authors">'+authors(items)+'</p>'
def render():
 data=json.loads((ROOT/'data/publications.json').read_text());cards=[];other=[]
 for p in data['publications']:
  links=''.join(f'<a href="{esc(x["url"])}">{esc(x["label"])} ↗</a>' for x in p['links'])
  if not p['selected']:continue
  visual=(f'<img src="{esc(p["image"])}" alt="{esc(p["title"])} — research illustration" loading="lazy">' if p.get('image') else '<div class="type-art"><span>SEED</span><b>3D 2.0</b><small>GEOMETRY · MATERIALS · SIMULATION</small></div>')
  cards.append(f'<article class="publication" id="{esc(p["id"])}"><div class="paper-art">{visual}</div><div class="paper-copy"><p class="eyebrow">{esc(p["venue"])} · {p["year"]}</p><h3><a href="{esc(p["links"][0]["url"])}">{esc(p["title"])}</a></h3>{author_block(p.get("core_contributors",p["authors"]),core=bool(p.get("core_contributors")))}<p class="summary">{esc(p["summary"])}</p><div class="paper-links">{links}</div></div></article>')
 return (ROOT/'data/page.html').read_text().replace('{{PUBLICATIONS}}','\n'.join(cards)).replace('{{OTHER}}','\n'.join(other))
if __name__=='__main__':
 import sys
 output=render();path=ROOT/'index.html'
 if '--check' in sys.argv:
  if path.read_text()!=output:raise SystemExit('index.html is stale; run python3 scripts/build.py')
 else:path.write_text(output)
