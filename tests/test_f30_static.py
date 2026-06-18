from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]
app=(root/'js/app.js').read_text(encoding='utf-8')
html=(root/'index.html').read_text(encoding='utf-8')
checks={
 'schema10':'schemaVersion:10' in app,
 'transport_def':"transportShip:{key:'transportShip'" in app,
 'coastal_fort':"coastalFort:{label:'Forte Costeiro'" in app,
 'embark_function':'function prepareEmbarkSelectedTroops' in app,
 'landing_function':'function launchAmphibiousLanding' in app,
 'enemy_invasion':'function spawnEnemyAmphibiousTransport' in app,
 'coastal_defense':'function updateCoastalDefense' in app,
 'transport_button':'data-ship="transportShip"' in html,
 'load_button':'id="btnLoadTroops"' in html,
 'landing_button':'id="btnLaunchLanding"' in html,
 'coastal_button':'data-building="coastalFort"' in html,
 'amphibious_data':(root/'data/naval/amphibious-operations.json').exists(),
}
missing=[k for k,v in checks.items() if not v]
report={'checks':checks,'missing':missing,'ok':not missing}
(root/'tests/RELATORIO_TESTE_ESTATICO_F30.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
(root/'tests/RELATORIO_TESTE_ESTATICO_F30.md').write_text('# Relatório estático — Fase 30\n\n'+ '\n'.join([f"- {k}: **{'OK' if v else 'FALHA'}**" for k,v in checks.items()])+f"\n\nResultado: **{'APROVADO' if not missing else 'FALHOU'}**\n",encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=False))
raise SystemExit(1 if missing else 0)
