from pathlib import Path
import json,re,sys
from html.parser import HTMLParser
root=Path(__file__).resolve().parents[1]
app=(root/'js/app.js').read_text(encoding='utf-8')
html=(root/'index.html').read_text(encoding='utf-8')
sw=(root/'service-worker.js').read_text(encoding='utf-8')
rg=(root/'js/release-guard.js').read_text(encoding='utf-8')
checks={
 'schema11':'schemaVersion:11' in app and 'schemaVersion=11' in rg,
 'coastal_state':'coastalSiege:null' in app,
 'coastal_wall':"coastalWall:{label:'Muralha Costeira'" in app,
 'beach_tower':"beachTower:{label:'Torre de Praia'" in app,
 'siege_workshop':"siegeWorkshop:{label:'Oficina de Cerco'" in app,
 'siege_ram':"siegeRam:{label:'Aríete de Cerco'" in app,
 'capture_update':'function updatePortCapture' in app,
 'siege_update':'function updateCoastalSiege' in app,
 'siege_draw':'function drawCoastalSiegeLayer' in app,
 'save_payload':'coastalSiege:serializeCoastalSiege()' in app,
 'wall_button':'data-building="coastalWall"' in html,
 'tower_button':'data-building="beachTower"' in html,
 'workshop_button':'data-building="siegeWorkshop"' in html,
 'ram_button':'data-unit="siegeRam"' in html,
 'locate_button':'id="btnLocateRivalPort"' in html,
 'stats':'id="portCaptureStat"' in html and 'id="portFortificationStat"' in html,
 'data_file':(root/'data/naval/coastal-siege.json').exists(),
 'pwa_cache':'coastal-siege.json' in sw and 'v3.7.0-f31' in sw,
}
# IDs duplicados
ids=re.findall(r'\bid=["\']([^"\']+)',html)
duplicates=sorted({i for i in ids if ids.count(i)>1})
checks['no_duplicate_ids']=not duplicates
# refs HTML/CSS
refs=[]
for pat in [r'\bsrc=["\']([^"\']+)',r'\bhref=["\']([^"\']+)']:
    refs.extend(re.findall(pat,html))
css=(root/'css/main.css').read_text(encoding='utf-8')
refs.extend(re.findall(r'url\(["\']?([^\)"\']+)',css))
missing=[]
for ref in refs:
    if ref.startswith(('http:','https:','data:','#','mailto:','javascript:')): continue
    ref=ref.split('?',1)[0].split('#',1)[0]
    if not ref: continue
    base=(root/'css') if ref.startswith('../') else root
    target=(base/ref).resolve()
    if not target.exists(): missing.append(ref)
checks['local_refs']=not missing
# JSON
bad_json=[]
for p in root.rglob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: bad_json.append(f'{p.relative_to(root)}: {e}')
checks['json_valid']=not bad_json
failed=[k for k,v in checks.items() if not v]
report={'checks':checks,'failed':failed,'duplicateIds':duplicates,'missingRefs':sorted(set(missing)),'badJson':bad_json,'ids':len(ids),'files':sum(1 for p in root.rglob('*') if p.is_file()),'ok':not failed}
(root/'tests/RELATORIO_TESTE_ESTATICO_F31.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
(root/'tests/RELATORIO_TESTE_ESTATICO_F31.md').write_text('# Relatório estático — Fase 31\n\n'+ '\n'.join([f"- {k}: **{'OK' if v else 'FALHA'}**" for k,v in checks.items()])+f"\n\nIDs: {len(ids)}  \nArquivos: {report['files']}  \nResultado: **{'APROVADO' if report['ok'] else 'FALHOU'}**\n",encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=False))
sys.exit(1 if failed else 0)
