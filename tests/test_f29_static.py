from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]
app=(root/'js/app.js').read_text(encoding='utf-8')
html=(root/'index.html').read_text(encoding='utf-8')
checks={
 'schema9':'schemaVersion:9' in app,
 'shipyard':"shipyard:{label:'Estaleiro Real'" in app,
 'naval_defs':'const NAVAL_UNIT_DEFS=' in app,
 'escort':"data-order=\"escort\"" in html,
 'blockade':"data-order=\"blockade\"" in html,
 'naval_context':'context-naval' in html,
 'naval_data':(root/'data/naval/military-fleet.json').exists(),
}
missing=[k for k,v in checks.items() if not v]
print(json.dumps({'checks':checks,'missing':missing},indent=2,ensure_ascii=False))
raise SystemExit(1 if missing else 0)
