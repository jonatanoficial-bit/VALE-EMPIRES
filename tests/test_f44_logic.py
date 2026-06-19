from pathlib import Path
root=Path(__file__).resolve().parents[1]

def test_f44_module_exposes_api():
    js=(root/'js/education-knowledge.js').read_text(encoding='utf-8')
    assert 'window.ValeEducationKnowledge' in js
    assert 'serialize:()=>normalize(knowledge)' in js
    assert 'score:knowledgeScore' in js
    assert 'localStorage.setItem(STORE' in js

def test_f44_has_actions_policies_institutions():
    js=(root/'js/education-knowledge.js').read_text(encoding='utf-8')
    for token in ['copyBooks','hireMasters','foundSchools','universityDebate','trainOfficials','workshopStandards']:
        assert token in js
    for token in ['templeSchools','civicLiteracy','royalUniversity','guildApprenticeship','stateExams']:
        assert token in js
    for token in ['villageSchools','scribalHalls','royalLibrary','universityCollege','artisanWorkshops','militaryAcademy']:
        assert token in js

def test_f44_integrations_are_optional():
    js=(root/'js/education-knowledge.js').read_text(encoding='utf-8')
    assert 'window.ValePublicHealth?.score?.()' in js
    assert 'window.ValeInternalEconomy?.score?.()' in js
    assert 'window.ValeReligionCivilization?.score?.()' in js
    assert 'window.ValeImperialLogistics?.score?.()' in js
