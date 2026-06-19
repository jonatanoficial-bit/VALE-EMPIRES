from pathlib import Path
root=Path(__file__).resolve().parents[1]

def test_f45_module_exposes_api():
    js=(root/'js/justice-law.js').read_text(encoding='utf-8')
    assert 'window.ValeJusticeLaw' in js
    assert 'serialize:()=>normalize(justice)' in js
    assert 'score:justiceScore' in js
    assert 'localStorage.setItem(STORE' in js

def test_f45_has_actions_policies_institutions():
    js=(root/'js/justice-law.js').read_text(encoding='utf-8')
    for token in ['codifyLaws','appointJudges','patrolRoads','auditCourts','prisonReform','publicTrials','amnestyProgram']:
        assert token in js
    for token in ['customaryBalance','royalCode','publicJustice','strictOrder','restorativeLaw']:
        assert token in js
    for token in ['royalCourt','magistrates','civilWatch','notaryArchives','prisonWardens','localCouncils']:
        assert token in js

def test_f45_integrations_are_optional():
    js=(root/'js/justice-law.js').read_text(encoding='utf-8')
    assert 'window.ValeEducationKnowledge?.score?.()' in js
    assert 'window.ValeInternalEconomy?.score?.()' in js
    assert 'window.ValeReligionCivilization?.score?.()' in js
    assert 'window.ValePublicHealth?.score?.()' in js
    assert 'window.ValeImperialLogistics?.score?.()' in js
