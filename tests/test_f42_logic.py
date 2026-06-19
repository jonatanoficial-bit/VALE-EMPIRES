from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
JS=(ROOT/'js/imperial-logistics.js').read_text(encoding='utf-8')

def test_logistics_model_contains_core_metrics():
    for token in ['roadIntegrity','courierSpeed','warehouseCoverage','convoySafety','militaryMobility','regionalIntegration','maintenanceBurden','banditRisk','bottleneck','worksSupport']:
        assert token in JS

def test_logistics_model_has_actions_policies_and_export():
    for token in ['balancedWorks','militaryPriority','merchantPriority','localAutonomy','paveRoads','repairBridges','depotExpansion','patrolRoutes','courierPosts','winterWorks','exportModel']:
        assert token in JS

def test_logistics_public_api():
    assert 'window.ValeImperialLogistics' in JS
    assert 'serialize:()=>normalize(model)' in JS
    assert 'score:logisticsScore' in JS
    assert re.search(r'function\s+restore\(data\)', JS)
    assert re.search(r'function\s+newReign\(\)', JS)
