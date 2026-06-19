from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]

def test_f44_files_present():
    assert (root/'js/education-knowledge.js').exists()
    assert (root/'data/society/education-knowledge.json').exists()
    assert (root/'docs/EDUCACAO_CONHECIMENTO_F44.md').exists()

def test_f44_index_hooks():
    html=(root/'index.html').read_text(encoding='utf-8')
    assert 'btnEducationKnowledgePanel' in html
    assert 'js/education-knowledge.js' in html

def test_f44_save_hooks():
    app=(root/'js/app.js').read_text(encoding='utf-8')
    assert 'schemaVersion:26' in app
    assert 'educationKnowledge:window.ValeEducationKnowledge?.serialize?.()||null' in app
    assert 'window.ValeEducationKnowledge?.restore?.(s.educationKnowledge)' in app
    assert 'window.ValeEducationKnowledge?.newReign?.()' in app

def test_f44_data_json():
    data=json.loads((root/'data/society/education-knowledge.json').read_text(encoding='utf-8'))
    assert data['phase']==44
    assert data['saveIntegration']['key']=='educationKnowledge'
    assert data['saveIntegration']['saveSchema']==24
