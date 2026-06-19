from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def test_f43_build_metadata():
    build=json.loads((ROOT/'BUILD.json').read_text(encoding='utf-8'))
    assert build['version']=='v4.12.0'
    assert int(build['phase'])>=43
    assert build['saveSchema']>=23
    assert 'F46' in build['buildId'] or 'PUBLIC-HEALTH' in build['buildId']

def test_f43_files_and_hooks():
    index=(ROOT/'index.html').read_text(encoding='utf-8')
    app=(ROOT/'js/app.js').read_text(encoding='utf-8')
    sw=(ROOT/'service-worker.js').read_text(encoding='utf-8')
    assert 'btnPublicHealthPanel' in index
    assert 'js/public-health.js' in index
    assert 'data/society/public-health.json' in sw
    assert 'vale-empires-v4.12.0-f46-demography-urbanism' in sw
    assert 'publicHealth:window.ValePublicHealth?.serialize?.()||null' in app
    assert 'window.ValePublicHealth?.restore?.(s.publicHealth)' in app
    assert 'window.ValePublicHealth?.newReign?.()' in app
    assert 'schemaVersion:26' in app

def test_f43_data_file():
    data=json.loads((ROOT/'data/society/public-health.json').read_text(encoding='utf-8'))
    assert data['phase']==43
    assert data['saveIntegration']['key']=='publicHealth'
    assert data['saveIntegration']['saveSchema']==23
    assert len(data['networks'])>=6
    assert len(data['districts'])>=5
