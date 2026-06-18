from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
import re, json, sys
root=Path(__file__).resolve().parents[1]
errors=[]
html=(root/'index.html').read_text(encoding='utf-8')
soup=BeautifulSoup(html,'html.parser')
ids=[n.get('id') for n in soup.find_all(attrs={'id':True})]
dup=[k for k,v in Counter(ids).items() if v>1]
if dup: errors.append(f'IDs duplicados: {dup}')
refs=[]
for tag in soup.find_all(['img','script','link','source']):
    for attr in ('src','href'):
        v=tag.get(attr)
        if v and not re.match(r'^(https?:|data:|#|mailto:|javascript:)',v): refs.append(v)
css=(root/'css/main.css').read_text(encoding='utf-8')
for v in re.findall(r'url\(["\']?([^"\')]+)',css):
    if not re.match(r'^(https?:|data:)',v): refs.append(str(Path('css')/v))
for ref in refs:
    if not (root/ref).resolve().exists(): errors.append(f'Referência ausente: {ref}')
manifest=json.loads((root/'manifest.webmanifest').read_text(encoding='utf-8'))
for icon in manifest.get('icons',[]):
    if not (root/icon['src']).exists(): errors.append(f'Ícone PWA ausente: {icon["src"]}')
print(json.dumps({'files':sum(1 for p in root.rglob('*') if p.is_file()),'html_ids':len(ids),'references':len(refs),'errors':errors},indent=2,ensure_ascii=False))
sys.exit(1 if errors else 0)
