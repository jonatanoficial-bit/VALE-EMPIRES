from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parents[1]
index=(ROOT/'index.html').read_text(encoding='utf-8')
app=(ROOT/'js/app.js').read_text(encoding='utf-8')
release=(ROOT/'js/release-guard.js').read_text(encoding='utf-8')
sw=(ROOT/'service-worker.js').read_text(encoding='utf-8')
info=(ROOT/'js/information-warfare.js').read_text(encoding='utf-8')
data=json.loads((ROOT/'data/diplomacy/information-warfare.json').read_text(encoding='utf-8'))
build=json.loads((ROOT/'BUILD.json').read_text(encoding='utf-8'))
assert build['buildId']=='VE-4.4.0-F38'
assert build['saveSchema']==18
assert 'btnInfoWarfarePanel' in index
assert 'js/information-warfare.js' in index
assert 'btnInfoWarfarePanel' in release
assert 'informationWarfare' in app
assert 'schemaVersion:18' in app
assert 'ValeInformationWarfare' in info
assert './js/information-warfare.js' in sw
assert './data/diplomacy/information-warfare.json' in sw
assert data['phase']==38
assert data['system']=='informationWarfare'
print('F38 static checks OK')
