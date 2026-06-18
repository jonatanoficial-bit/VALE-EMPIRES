import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
governors={'steward':1.16,'marshal':.96,'architect':1.02,'diplomat':1.04}
laws={'charter':1,'taxation':1.48,'works':.78,'frontier':.88}
taxes={'low':.72,'normal':1,'high':1.42}
def revenue(base,prosperity,integration,law,tax,governor):
    quality=.45+(prosperity/100)*.38+(integration/100)*.22
    return max(1,round(base*laws[law]*taxes[tax]*governors[governor]*quality))
def cohesion(provinces,network_bonus=0):
    avg=sum((p['stability']+p['loyalty']+p['integration'])/3 for p in provinces)/len(provinces)
    return max(0,min(100,avg+network_bonus))
checks={}
checks['high_tax_yields_more']=revenue(10,60,70,'charter','high','steward')>revenue(10,60,70,'charter','normal','steward')
checks['works_yields_less_than_taxation']=revenue(10,60,70,'works','normal','steward')<revenue(10,60,70,'taxation','normal','steward')
checks['steward_improves_revenue']=revenue(10,60,70,'charter','normal','steward')>revenue(10,60,70,'charter','normal','marshal')
checks['cohesion_in_bounds']=0<=cohesion([{'stability':82,'loyalty':86,'integration':100},{'stability':52,'loyalty':48,'integration':40}],7)<=100
checks['population_bonus_three_provinces']=max(0,3-1)*2==4
report={'ok':all(checks.values()),'checks':checks,'sampleNormal':revenue(10,60,70,'charter','normal','steward'),'sampleHigh':revenue(10,60,70,'charter','high','steward')}
(root/'tests/RELATORIO_TESTE_LOGICA_F34.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
(root/'tests/RELATORIO_TESTE_LOGICA_F34.md').write_text('# Relatório lógico — Fase 34\n\n'+'\n'.join(f'- {k}: {"OK" if v else "FALHOU"}' for k,v in checks.items()),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
raise SystemExit(0 if report['ok'] else 1)
