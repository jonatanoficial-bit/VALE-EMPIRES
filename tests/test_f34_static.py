from pathlib import Path
from bs4 import BeautifulSoup
import json,re,sys
root=Path(__file__).resolve().parents[1]
errors=[]
build=json.loads((root/'BUILD.json').read_text(encoding='utf-8'))
if build.get('version')!='v4.0.0': errors.append('versão incorreta')
if build.get('saveSchema')!=14: errors.append('save schema incorreto')
app=(root/'js/app.js').read_text(encoding='utf-8')
for token in ['defaultProvinceNetwork','serializeProvinceNetwork','initializeProvinceNetwork','updateProvinceNetwork','provinceTaxTick','openProvincePanel','schemaVersion:14','provinceNetwork:serializeProvinceNetwork()','provincePopulationBonus']:
    if token not in app: errors.append(f'ausente: {token}')
html=(root/'index.html').read_text(encoding='utf-8')
soup=BeautifulSoup(html,'html.parser')
ids=[x.get('id') for x in soup.find_all(attrs={'id':True})]
dups=sorted({x for x in ids if ids.count(x)>1})
if dups: errors.append('IDs duplicados: '+','.join(dups))
required=['btnCityAdminPanel','cityStabilityStat','cityLoyaltyStat','btnProvincePanel','provinceCountStat','provinceGovernorStat','provinceCohesionStat','provinceIncomeStat','provinceConnectionsStat','provinceTaxCyclesStat']
for rid in required:
    if rid not in ids: errors.append(f'ID ausente: {rid}')
refs=[]
for tag in soup.find_all(True):
    for attr in ('src','href'):
        v=tag.get(attr)
        if v and not re.match(r'^(?:https?:|data:|#|mailto:|javascript:)',v): refs.append(v.split('?')[0])
for ref in refs:
    if not (root/ref).exists(): errors.append(f'referência HTML ausente: {ref}')
sw=(root/'service-worker.js').read_text(encoding='utf-8')
for ref in re.findall(r"'\./([^']+)'",sw):
    if ref and not (root/ref).exists(): errors.append(f'cache ausente: {ref}')
for p in root.rglob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'JSON inválido {p.relative_to(root)}: {e}')
report={'ok':not errors,'build':build.get('buildId'),'htmlIds':len(ids),'duplicateIds':dups,'htmlRefs':len(refs),'jsonFiles':len(list(root.rglob('*.json'))),'errors':errors}
(root/'tests/RELATORIO_TESTE_ESTATICO_F34.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
(root/'tests/RELATORIO_TESTE_ESTATICO_F34.md').write_text('# Relatório estático — Fase 34\n\n'+('\n'.join('- '+e for e in errors) if errors else '- Todos os testes estáticos passaram.'),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
sys.exit(1 if errors else 0)
