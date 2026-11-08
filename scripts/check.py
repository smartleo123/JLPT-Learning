import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1];d=json.loads((root/'data/study.json').read_text());s=(root/'index.html').read_text()
assert len(d['coverage'])==31
assert len({x['id'] for x in d['items']})==len(d['items'])
assert len({(x['type'],x['term']) for x in d['items']})==len(d['items'])
for x in d['items']:
 assert all(x[k] for k in ['meaning','pitfall','example','sources','category'])
 assert x['count']==len({z['session'] for z in x['sources']})==len(x['sources'])
 assert x['recentCount']==sum(z['session']>='2022' for z in x['sources'])
 for z in x['sources']:
  assert z['page']>0 and 'url' not in z
 if x['type']=='grammar': assert x['connection']
 else: assert x['reading']
embedded=json.loads(re.search(r'<script id="study-data" type="application/json">(.*?)</script>',s,re.S).group(1));assert embedded==d
for k in ['styles.css','app.js','METHOD.md','data/study.json']:assert(root/k).is_file()
assert not re.search(r'__[A-Z]+__',s)
assert 'drive.google.com' not in s
assert 'drive.google.com' not in (root/'data/study.json').read_text()
print(f'PASS: {len(d["items"])} unique entries, 31 sources, count invariants, embedded data and local assets')
