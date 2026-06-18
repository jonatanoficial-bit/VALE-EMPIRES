from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parents[1]
html=(ROOT/'index.html').read_text(encoding='utf-8')
app=(ROOT/'js/app.js').read_text(encoding='utf-8')
rg=(ROOT/'js/release-guard.js').read_text(encoding='utf-8')
sw=(ROOT/'service-worker.js').read_text(encoding='utf-8')
assert 'btnCulturalMoralePanel' in html
assert 'js/cultural-morale.js' in html
assert 'js/cultural-morale.js' in sw
assert 'data/society/cultural-morale.json' in sw
assert 'culturalMorale:window.ValeCulturalMorale' in app
assert 'ValeCulturalMorale?.restore' in app
assert 'schemaVersion:19' in app
assert 'migrated.schemaVersion=19' in rg
assert 'culturalMorale' in rg
json.loads((ROOT/'data/society/cultural-morale.json').read_text(encoding='utf-8'))
print('F39 static OK')
