from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def test_f42_build_metadata():
    build=json.loads((ROOT/'BUILD.json').read_text(encoding='utf-8'))
    assert build['version']=='v4.12.0'
    assert int(build['phase'])>=42
    assert build['saveSchema']>=22
    assert 'F46' in build['buildId'] or 'IMPERIAL-LOGISTICS' in build['buildId']

def test_f42_files_and_hooks():
    index=(ROOT/'index.html').read_text(encoding='utf-8')
    app=(ROOT/'js/app.js').read_text(encoding='utf-8')
    sw=(ROOT/'service-worker.js').read_text(encoding='utf-8')
    assert 'btnImperialLogisticsPanel' in index
    assert 'js/imperial-logistics.js' in index
    assert 'data/infrastructure/imperial-logistics.json' in sw
    assert 'vale-empires-v4.12.0-f46-demography-urbanism' in sw
    assert 'imperialLogistics:window.ValeImperialLogistics?.serialize?.()||null' in app
    assert 'window.ValeImperialLogistics?.restore?.(s.imperialLogistics)' in app
    assert 'window.ValeImperialLogistics?.newReign?.()' in app
    assert 'schemaVersion:26' in app

def test_f42_data_file():
    data=json.loads((ROOT/'data/infrastructure/imperial-logistics.json').read_text(encoding='utf-8'))
    assert data['phase']==42
    assert data['saveIntegration']['key']=='imperialLogistics'
    assert data['saveIntegration']['saveSchema']==22
    assert len(data['networks'])>=6
    assert len(data['corridors'])>=5
