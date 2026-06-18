from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parents[1]
html=(ROOT/'index.html').read_text(encoding='utf-8')
app=(ROOT/'js/app.js').read_text(encoding='utf-8')
rg=(ROOT/'js/release-guard.js').read_text(encoding='utf-8')
sw=(ROOT/'service-worker.js').read_text(encoding='utf-8')
assert 'btnSecretOpsPanel' in html
assert 'js/secret-operations.js' in html
assert 'secretOperations:window.ValeSecretOperations?.serialize?.()||null' in app
assert 'ValeSecretOperations?.restore' in app
assert 'ValeSecretOperations?.newReign' in app
assert 'schemaVersion:17' in app
assert 'migrated.secretOperations' in rg
assert 'migrated.schemaVersion=17' in rg
assert './js/secret-operations.js' in sw
assert './data/intelligence/secret-operations.json' in sw
json.loads((ROOT/'data/intelligence/secret-operations.json').read_text(encoding='utf-8'))
print('F37 static checks OK')
