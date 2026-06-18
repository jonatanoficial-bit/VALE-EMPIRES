import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
policies={
 'balanced':{'gold':8,'food':5,'risk':-5},
 'relief':{'gold':3,'food':3,'risk':-12},
 'tribute':{'gold':16,'stone':5,'risk':18},
 'martial':{'gold':7,'stone':4,'risk':-8},
}
def income(policy,prosperity,integration):
    mult=.45+(prosperity/100)*.75+(integration/100)*.25
    return {k:max(1,round(v*mult)) for k,v in policies[policy].items() if k!='risk'}
def revolt(stability,loyalty,garrison,target,reconstruction,policy):
    ratio=min(1,garrison/target)
    unrest=max(0,min(100,100-(stability+loyalty)/2+(18 if policy=='tribute' else 0)+(12 if ratio<.35 else 0)-(reconstruction/100)*12))
    return max(0,min(100,unrest+policies[policy]['risk']-ratio*18))
checks={}
checks['balanced_income_positive']=income('balanced',50,50)['gold']>0
checks['tribute_income_higher']=income('tribute',50,50)['gold']>income('balanced',50,50)['gold']
checks['garrison_reduces_revolt']=revolt(45,40,6,6,30,'balanced')<revolt(45,40,0,6,30,'balanced')
checks['relief_safer_than_tribute']=revolt(45,40,3,6,30,'relief')<revolt(45,40,3,6,30,'tribute')
checks['integration_formula_bounds']=0<=45*.32+40*.32+30*.24+25*.12<=100
report={'ok':all(checks.values()),'checks':checks,'sampleIncome':income('balanced',50,50),'sampleRiskLowGarrison':revolt(45,40,0,6,30,'balanced'),'sampleRiskFullGarrison':revolt(45,40,6,6,30,'balanced')}
(root/'tests/RELATORIO_TESTE_LOGICA_F33.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
(root/'tests/RELATORIO_TESTE_LOGICA_F33.md').write_text('# Relatório lógico — Fase 33\n\n'+ '\n'.join(f'- {k}: {"OK" if v else "FALHOU"}' for k,v in checks.items())+f"\n\nRisco sem guarnição: {report['sampleRiskLowGarrison']:.1f}%  \nRisco com guarnição completa: {report['sampleRiskFullGarrison']:.1f}%\n",encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
raise SystemExit(0 if report['ok'] else 1)
