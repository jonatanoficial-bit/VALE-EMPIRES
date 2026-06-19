from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
JS = (ROOT / 'js/religion-civilization.js').read_text(encoding='utf-8')

def extract_object_names(name):
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


def test_stability_formula_contains_advanced_inputs():
    assert 'function popularStability()' in JS
    for token in ['cultureScore()', 'provinceCohesion', "factionAverage('support')", "factionAverage('tension')", 'model.identity', 'model.memory', 'model.unrest']:
        assert token in JS


def test_identity_and_faction_systems_exist():
    for token in ['function nationalIdentity()', 'function mediateFaction', 'function strengthenTradition', 'function setCharter', 'function runAction']:
        assert token in JS
    assert len(re.findall(r"id:'[a-zA-Z]+',name", extract_object_names('factions'))) >= 6
    assert len(re.findall(r"id:'[a-zA-Z]+',name", extract_object_names('traditions'))) >= 5
    assert len(re.findall(r"id:'[a-zA-Z]+',label", extract_object_names('actions'))) >= 7


def test_no_real_religion_dependency():
    lowered = JS.lower()
    forbidden = ['christianity', 'islam', 'judaism', 'hinduism', 'buddhism']
    assert not any(word in lowered for word in forbidden)
    assert 'ficcional' in lowered or 'fictional' in lowered
