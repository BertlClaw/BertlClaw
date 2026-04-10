#!/usr/bin/env python3
from pathlib import Path
import csv, json, re, sys
ROOT = Path(__file__).resolve().parent.parent
master = ROOT / 'data' / 'sitemap-master.csv'
if not master.exists():
    print('missing data/sitemap-master.csv', file=sys.stderr)
    sys.exit(1)
rows=[]
for row in csv.DictReader(master.open(encoding='utf-8')):
    rel=row['local_file']
    p=ROOT / rel
    result=dict(row)
    result['exists']=p.exists()
    result['valid']=False
    result['issues']=[]
    if p.exists():
        txt=p.read_text(encoding='utf-8', errors='ignore')
        low=txt.lower()
        if '<title' not in low: result['issues'].append('missing_title')
        if 'meta name="description"' not in low and "meta name='description'" not in low: result['issues'].append('missing_meta_description')
        if '<h1' not in low: result['issues'].append('missing_h1')
        if 'rel="canonical"' not in low and "rel='canonical'" not in low: result['issues'].append('missing_canonical')
        text_only=re.sub(r'<[^>]+>', ' ', txt)
        text_only=re.sub(r'\s+', ' ', text_only).strip()
        if len(text_only) < 500: result['issues'].append('thin_content')
        result['valid']=len(result['issues'])==0
    else:
        result['issues'].append('missing_file')
    rows.append(result)
out_json=ROOT/'data'/'sitemap-validation.json'
out_csv=ROOT/'data'/'sitemap-validation.csv'
json.dump({'count':len(rows),'valid':sum(1 for r in rows if r['valid']),'invalid':sum(1 for r in rows if not r['valid']),'items':rows}, out_json.open('w',encoding='utf-8'), ensure_ascii=False, indent=2)
with out_csv.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f, fieldnames=['url','local_file','kind','status','exists','valid','issues'])
    w.writeheader()
    for r in rows:
        rr={k:r.get(k) for k in ['url','local_file','kind','status','exists','valid']}
        rr['issues']='|'.join(r['issues'])
        w.writerow(rr)
print(json.dumps({'count':len(rows),'valid':sum(1 for r in rows if r['valid']),'invalid':sum(1 for r in rows if not r['valid'])}, indent=2))
