from pathlib import Path
import json, re, sys
root=Path(__file__).resolve().parents[1]
app=(root/'js/app.js').read_text(encoding='utf-8')
html=(root/'index.html').read_text(encoding='utf-8')
build=json.loads((root/'BUILD.json').read_text(encoding='utf-8'))
checks={
 'build v3.2.0': build.get('version')=='v3.2.0',
 'fase 26': build.get('phase')=='26',
 'schema 6': build.get('saveSchema')==6 and 'schemaVersion:6' in app,
 'painel diplomacia': 'id="diplomacyOverlay"' in html and 'id="btnDiplomacyPanel"' in html,
 'cinco facções': 'Object.keys(NATION_DEFS).filter(id=>id!==player)' in app,
 'comércio': "action==='trade'" in app and 'diplomacyPassiveTick' in app,
 'aliança': "action==='alliance'" in app and 'diplomacyPopulationBonus' in app,
 'trégua': "action==='truce'" in app and 'isRivalHostile' in app,
 'save diplomacia': 'diplomacy:serializeDiplomacy()' in app and 'initializeDiplomacy(s.diplomacy)' in app,
 'dados diplomáticos': (root/'data/diplomacy/diplomatic-profiles.json').exists(),
}
for name,ok in checks.items(): print(('OK' if ok else 'FAIL'),name)
if not all(checks.values()): sys.exit(1)
