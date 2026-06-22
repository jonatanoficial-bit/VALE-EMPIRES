from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def test_f48_files_and_hooks():
    assert (ROOT/'js/external-commerce.js').exists()
    assert (ROOT/'data/trade/external-commerce.json').exists()
    html=(ROOT/'index.html').read_text(encoding='utf-8')
    assert 'btnExternalCommercePanel' in html
    assert 'js/external-commerce.js' in html
    app=(ROOT/'js/app.js').read_text(encoding='utf-8')
    assert 'schemaVersion:27' in app
    assert 'externalCommerce:window.ValeExternalCommerce?.serialize?.()||null' in app
    assert 'window.ValeExternalCommerce?.restore?.(s.externalCommerce)' in app
    sw=(ROOT/'service-worker.js').read_text(encoding='utf-8')
    assert 'external-commerce.js' in sw
    assert 'external-commerce.json' in sw

def test_f48_json_data_valid():
    data=json.loads((ROOT/'data/trade/external-commerce.json').read_text(encoding='utf-8'))
    assert data['phase']==48
    assert data['saveKey']=='externalCommerce'
    assert len(data['markets'])>=5
