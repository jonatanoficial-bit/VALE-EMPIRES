from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def test_phase_40_files_and_hooks():
    html = (ROOT / 'index.html').read_text(encoding='utf-8')
    app = (ROOT / 'js/app.js').read_text(encoding='utf-8')
    guard = (ROOT / 'js/release-guard.js').read_text(encoding='utf-8')
    sw = (ROOT / 'service-worker.js').read_text(encoding='utf-8')
    assert 'btnReligionCivilizationPanel' in html
    assert 'js/religion-civilization.js' in html
    assert 'data/society/religion-civilization.json' in sw
    assert 'religionCivilization' in app
    assert 'ValeReligionCivilization?.serialize' in app
    assert 'ValeReligionCivilization?.restore' in app
    assert 'religionCivilization' in guard
    assert 'schemaVersion=21' in guard or 'schemaVersion=20' in guard


def test_phase_40_dataset():
    data = json.loads((ROOT / 'data/society/religion-civilization.json').read_text(encoding='utf-8'))
    assert data['phase'] == 40
    assert data['version'] == 'v4.6.1'
    assert data['saveIntegration']['mainSaveField'] == 'religionCivilization'
    assert 'faccoes_sociais' in data['systems']
    assert len(data['civilizationCharters']) == 4
    assert len(data['traditions']) >= 5
    assert len(data['socialFactions']) >= 6
    assert len(data['actions']) >= 7


def test_show_guard_for_missing_screens():
    app = (ROOT / 'js/app.js').read_text(encoding='utf-8')
    assert 'if(!e)return' in app
    assert 'Tela solicitada ausente' in app
    assert 'screens[name]?name' in app
