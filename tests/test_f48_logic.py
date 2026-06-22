from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
JS=(ROOT/'js/external-commerce.js').read_text(encoding='utf-8')

def test_f48_public_api_and_metrics():
    assert 'window.ValeExternalCommerce' in JS
    for token in ['commerceScore','exportCapacity','importDependency','foreignTrust','treatyNetwork','embargoRisk','contraband']:
        assert token in JS

def test_f48_actions_exist():
    for action in ['negotiateTreaty','openForeignMarket','secureConvoys','counterSmuggling','strategicEmbargo','exportSubsidy']:
        assert action in JS

def test_f48_has_no_obvious_bad_precedence_bug():
    assert 'commerce.contraband+.08+commerce.tariffEfficiency<40?1.2:0' not in JS
    assert 'commerce.contraband+.08+(commerce.tariffEfficiency<40?1.2:0)' in JS
