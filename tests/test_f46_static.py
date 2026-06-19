from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]

def test_f46_files_present():
    assert (root/'js/demography-urbanism.js').exists()
    assert (root/'data/society/demography-urbanism.json').exists()
    assert (root/'docs/DEMOGRAFIA_MIGRACAO_URBANISMO_F46.md').exists()

def test_f46_index_hooks():
    html=(root/'index.html').read_text(encoding='utf-8')
    assert 'btnDemographyUrbanismPanel' in html
    assert 'js/demography-urbanism.js' in html

def test_f46_save_hooks():
    app=(root/'js/app.js').read_text(encoding='utf-8')
    assert 'schemaVersion:26' in app
    assert 'demographyUrbanism:window.ValeDemographyUrbanism?.serialize?.()||null' in app
    assert 'window.ValeDemographyUrbanism?.restore?.(s.demographyUrbanism)' in app
    assert 'window.ValeDemographyUrbanism?.newReign?.()' in app

def test_f46_data_json():
    data=json.loads((root/'data/society/demography-urbanism.json').read_text(encoding='utf-8'))
    assert data['phase']==46
    assert data['saveIntegration']['key']=='demographyUrbanism'
    assert data['saveIntegration']['saveSchema']==26
