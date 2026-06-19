from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]

def test_f45_files_present():
    assert (root/'js/justice-law.js').exists()
    assert (root/'data/society/justice-law.json').exists()
    assert (root/'docs/JUSTICA_LEIS_ORDEM_CIVIL_F45.md').exists()

def test_f45_index_hooks():
    html=(root/'index.html').read_text(encoding='utf-8')
    assert 'btnJusticeLawPanel' in html
    assert 'js/justice-law.js' in html

def test_f45_save_hooks():
    app=(root/'js/app.js').read_text(encoding='utf-8')
    assert 'schemaVersion:26' in app
    assert 'justiceLaw:window.ValeJusticeLaw?.serialize?.()||null' in app
    assert 'window.ValeJusticeLaw?.restore?.(s.justiceLaw)' in app
    assert 'window.ValeJusticeLaw?.newReign?.()' in app

def test_f45_data_json():
    data=json.loads((root/'data/society/justice-law.json').read_text(encoding='utf-8'))
    assert data['phase']==45
    assert data['saveIntegration']['key']=='justiceLaw'
    assert data['saveIntegration']['saveSchema']==25
