from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
JS=(ROOT/'js/public-health.js').read_text(encoding='utf-8')

def test_public_health_model_contains_core_metrics():
    for token in ['sanitation','cleanWater','hospitalCapacity','healers','foodSafety','medicine','diseaseSurveillance','wellbeing','epidemicRisk','crowding','quarantineSupport']:
        assert token in JS

def test_public_health_has_actions_policies_and_export():
    for token in ['preventiveCare','emergencyQuarantine','templeHospitals','guildMedicine','digWells','cleanStreets','buildInfirmary','trainHealers','inspectMarkets','cordonSanitary','exportModel']:
        assert token in JS

def test_public_health_public_api():
    assert 'window.ValePublicHealth' in JS
    assert 'serialize:()=>normalize(health)' in JS
    assert 'score:healthScore' in JS
    assert re.search(r'function\s+restore\(data\)', JS)
    assert re.search(r'function\s+newReign\(\)', JS)
