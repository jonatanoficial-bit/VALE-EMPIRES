from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def test_phase_41_files_and_hooks():
    html = (ROOT / 'index.html').read_text(encoding='utf-8')
    app = (ROOT / 'js/app.js').read_text(encoding='utf-8')
    guard = (ROOT / 'js/release-guard.js').read_text(encoding='utf-8')
    sw = (ROOT / 'service-worker.js').read_text(encoding='utf-8')
    build = json.loads((ROOT / 'BUILD.json').read_text(encoding='utf-8'))
    assert build['phase'] == '41'
    assert build['version'] == 'v4.7.0'
    assert build['saveSchema'] == 21
    assert 'btnInternalEconomyPanel' in html
    assert 'js/internal-economy.js' in html
    assert 'data/economy/internal-economy.json' in sw
    assert 'internalEconomy' in app
    assert 'ValeInternalEconomy?.serialize' in app
    assert 'ValeInternalEconomy?.restore' in app
    assert 'ValeInternalEconomy?.newReign' in app
    assert 'internalEconomy' in guard
    assert 'schemaVersion=21' in guard


def test_phase_41_dataset():
    data = json.loads((ROOT / 'data/economy/internal-economy.json').read_text(encoding='utf-8'))
    assert data['phase'] == 41
    assert data['version'] == 'v4.7.0'
    assert data['saveIntegration']['mainSaveField'] == 'internalEconomy'
    assert data['saveIntegration']['saveSchema'] == 21
    assert 'mercado_domestico' in data['systems']
    assert len(data['fiscalPolicies']) >= 4
    assert len(data['productiveSectors']) >= 4
    assert len(data['productiveClasses']) >= 6
    assert len(data['economicActions']) >= 7


def test_f40_recovery_hotfix_still_preserved():
    app = (ROOT / 'js/app.js').read_text(encoding='utf-8')
    sw = (ROOT / 'service-worker.js').read_text(encoding='utf-8')
    assert 'if(!e)return' in app
    assert 'Tela solicitada ausente' in app
    assert 'vale-empires-v4.7.0-f41-internal-economy' in sw
