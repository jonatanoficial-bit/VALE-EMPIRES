from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
JS = (ROOT / 'js/internal-economy.js').read_text(encoding='utf-8')

def extract_object(name):
    marker = f"const {name}={{"
    assert marker in JS
    start = JS.index(marker) + len(marker) - 1
    depth = 0
    for i in range(start, len(JS)):
        if JS[i] == '{':
            depth += 1
        elif JS[i] == '}':
            depth -= 1
            if depth == 0:
                return JS[start:i+1]
    raise AssertionError(f'object {name} not closed')


def test_economic_health_formula_has_advanced_inputs():
    assert 'function economicHealth()' in JS
    for token in ['economy.prosperity', 'economy.supply', 'economy.confidence', 'economy.liquidity', 'socialScore()', 'identityScore()', "classAverage('support')", 'economy.priceIndex', 'economy.taxPressure', 'economy.corruption', 'economy.blackMarket', 'economy.unemployment']:
        assert token in JS


def test_productive_economy_systems_exist():
    for token in ['function setPolicy', 'function investSector', 'function runAction', 'function tick', 'function chance', 'function applyEffect']:
        assert token in JS
    assert len(re.findall(r"id:'[a-zA-Z]+',label", extract_object('policies'))) >= 4
    assert len(re.findall(r"id:'[a-zA-Z]+',icon", extract_object('sectors'))) >= 4
    assert len(re.findall(r"id:'[a-zA-Z]+',icon", extract_object('classes'))) >= 6
    assert len(re.findall(r"id:'[a-zA-Z]+',label", extract_object('actions'))) >= 7


def test_integration_with_existing_realm_layers():
    for token in ['ValeEmpiresAPI', 'ValeReligionCivilization?.score', 'ValeReligionCivilization?.identity', 'ValeCulturalMorale?.score', 'getSnapshot', 'addStock', 'spend', 'saveQuiet']:
        assert token in JS
    assert 'valeEmpires.internalEconomy' in JS
    assert 'window.ValeInternalEconomy' in JS
