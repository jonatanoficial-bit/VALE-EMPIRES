from pathlib import Path
root=Path(__file__).resolve().parents[1]

def test_f46_module_exposes_api():
    js=(root/'js/demography-urbanism.js').read_text(encoding='utf-8')
    assert 'window.ValeDemographyUrbanism' in js
    assert 'serialize:()=>normalize(demo)' in js
    assert 'score:demoScore' in js
    assert 'localStorage.setItem(STORE' in js

def test_f46_has_actions_policies_districts():
    js=(root/'js/demography-urbanism.js').read_text(encoding='utf-8')
    for token in ['buildHousing','openGranaryNeighborhoods','registerMigrants','planStreets','promoteFamilies','relocateOvercrowded','civicFestival']:
        assert token in js
    for token in ['balancedSettlement','openFrontier','urbanCharter','familyRelief','assimilation']:
        assert token in js
    for token in ['capitalQuarter','workersWard','migrantCamp','familyHomes','frontierVillages','publicSquares']:
        assert token in js

def test_f46_integrations_are_optional():
    js=(root/'js/demography-urbanism.js').read_text(encoding='utf-8')
    assert 'window.ValePublicHealth?.score?.()' in js
    assert 'window.ValeInternalEconomy?.score?.()' in js
    assert 'window.ValeImperialLogistics?.score?.()' in js
    assert 'window.ValeJusticeLaw?.score?.()' in js
    assert 'window.ValeEducationKnowledge?.score?.()' in js
    assert 'window.ValeReligionCivilization?.score?.()' in js
