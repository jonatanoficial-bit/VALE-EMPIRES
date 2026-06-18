from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
import json,re,sys

ROOT=Path(__file__).resolve().parents[1]
errors=[]
checks=[]

def check(condition,label):
    checks.append({'check':label,'ok':bool(condition)})
    if not condition: errors.append(label)

html=(ROOT/'index.html').read_text(encoding='utf-8')
soup=BeautifulSoup(html,'html.parser')
ids=[n.get('id') for n in soup.find_all(attrs={'id':True})]
check(not [k for k,v in Counter(ids).items() if v>1],'HTML sem IDs duplicados')
for req in ['btnSkirmishMenu','skirmishScreen','btnSkirmishStart','skirmishSeed','skirmishResultOverlay','btnSkirmishResultRestart']:
    check(soup.find(id=req) is not None,f'ID obrigatório presente: {req}')

expected={'mapSize':3,'startingEra':4,'resources':3,'victory':3,'difficulty':5}
for group,count in expected.items():
    found=soup.select(f'.skirmish-choice[data-skirmish-group="{group}"]')
    check(len(found)==count,f'{group}: {count} opções')

app=(ROOT/'js/app.js').read_text(encoding='utf-8')
for fn in ['openSkirmishSetup','startSkirmish','updateSkirmish','finishSkirmish','skirmishProgress','normalizeSkirmishConfig']:
    check(f'function {fn}' in app,f'Função presente: {fn}')
check('schemaVersion:5' in app,'Save schema 5 no app')
check("'valeEmpires.save.skirmish'" in app,'Slot dedicado de save da partida livre')
check("'valeEmpires.save.campaign'" in app,'Slot dedicado de save da campanha')
check("state.gameMode==='skirmish'" in app,'Roteamento por modo de jogo')
check("SKIRMISH_MAP_DEFS[state.skirmish?.mapSize]" in app,'Tamanho de mapa aplicado na geração')
check("state.gameMode==='skirmish'?openSkirmishPanel():openMissionPanel()" in app,'Painel contextual da partida livre')

build=json.loads((ROOT/'BUILD.json').read_text(encoding='utf-8'))
check(build.get('version')=='v3.1.0','Versão v3.1.0')
check(build.get('phase')=='25','Fase 25')
check(build.get('saveSchema')==5,'BUILD saveSchema 5')

# i18n parity
locale_files={}
for loc in ['pt-BR','en-US','es-ES']:
    locale_files[loc]=json.loads((ROOT/'locales'/f'{loc}.json').read_text(encoding='utf-8'))
base_keys=set(locale_files['pt-BR']['keys'])
base_text=set(locale_files['pt-BR']['text'])
for loc,data in locale_files.items():
    check(set(data['keys'])==base_keys,f'Paridade de keys: {loc}')
    check(set(data['text'])==base_text,f'Paridade de textos-base: {loc}')
    check(data['keys'].get('menu.skirmish') is not None,f'Tradução menu.skirmish: {loc}')

# HTML/CSS refs
refs=[]
for tag in soup.find_all(['img','script','link','source']):
    for attr in ['src','href']:
        val=tag.get(attr)
        if val and not re.match(r'^(?:https?:|data:|#|mailto:|javascript:)',val): refs.append(val)
css=(ROOT/'css/main.css').read_text(encoding='utf-8')
for val in re.findall(r'url\(["\']?([^"\')]+)',css):
    if not re.match(r'^(?:https?:|data:)',val): refs.append(str(Path('css')/val))
missing=[]
for ref in refs:
    target=(ROOT/ref).resolve()
    if not target.exists(): missing.append(ref)
check(not missing,'Referências HTML/CSS existentes')

# service worker core assets
sw=(ROOT/'service-worker.js').read_text(encoding='utf-8')
core_match=re.search(r'const CORE_ASSETS=(\[.*?\]);',sw,re.S)
check(core_match is not None,'CORE_ASSETS encontrado')
missing_core=[]
core_count=0
if core_match:
    core=json.loads(core_match.group(1).replace("'",'"'))
    core_count=len(core)
    for ref in core:
        rel=ref[2:] if ref.startswith('./') else ref
        if rel in ('','./'): continue
        if not (ROOT/rel).exists(): missing_core.append(ref)
check(not missing_core,'Cache PWA sem arquivos ausentes')
check("vale-empires-v3.1.0-f25-skirmish" in sw,'Cache PWA versionado para F25')

report={
    'phase':'25','version':'v3.1.0','files':sum(1 for p in ROOT.rglob('*') if p.is_file()),
    'html_ids':len(ids),'html_css_references':len(refs),'pwa_core_assets':core_count,
    'locale_base_keys':len(base_keys),'locale_base_texts':len(base_text),
    'checks':checks,'errors':errors,'missing_references':missing,'missing_core_assets':missing_core
}
print(json.dumps(report,indent=2,ensure_ascii=False))
(ROOT/'tests'/'RELATORIO_TESTE_ESTATICO_F25.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
sys.exit(1 if errors else 0)
