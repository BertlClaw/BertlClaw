#!/usr/bin/env python3
from pathlib import Path
import csv, xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parent.parent
master = ROOT/'data'/'sitemap-master.csv'
ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
ns='http://www.sitemaps.org/schemas/sitemap/0.9'
by_kind={}
rows=list(csv.DictReader(master.open(encoding='utf-8')))
for row in rows:
    by_kind.setdefault(row['kind'], []).append(row)
for kind, items in by_kind.items():
    urlset=ET.Element(f'{{{ns}}}urlset')
    for item in items:
        u=ET.SubElement(urlset, f'{{{ns}}}url')
        loc=ET.SubElement(u, f'{{{ns}}}loc')
        loc.text=item['url']
    ET.ElementTree(urlset).write(ROOT/f'sitemap-{kind}.xml', encoding='utf-8', xml_declaration=True)
index=ET.Element(f'{{{ns}}}sitemapindex')
for kind in sorted(by_kind):
    sm=ET.SubElement(index, f'{{{ns}}}sitemap')
    loc=ET.SubElement(sm, f'{{{ns}}}loc')
    loc.text=f'https://bertlclaw.at/sitemap-{kind}.xml'
ET.ElementTree(index).write(ROOT/'sitemap-index.xml', encoding='utf-8', xml_declaration=True)
print('built', len(by_kind), 'sitemaps')
