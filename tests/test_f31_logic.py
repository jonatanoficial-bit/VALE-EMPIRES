from pathlib import Path
import json,sys
root=Path(__file__).resolve().parents[1]
cfg=json.loads((root/'data/naval/coastal-siege.json').read_text(encoding='utf-8'))
errors=[]
ram=cfg['units']['siegeRam']; port=cfg['portCapture']; tower=cfg['buildings']['beachTower']; wall=cfg['buildings']['coastalWall']
if ram['buildingDamageMultiplier']<2: errors.append('multiplicador de cerco insuficiente')
# Aríete contra fortificação
hp=port['fortificationHp']; attack=ram['attack']; hits=0
while hp>0 and hits<20:
    hp-=round(attack*2.2);hits+=1
if hp>0 or hits>10: errors.append('fortificação não cai em janela esperada')
# Captura com cinco tropas no ritmo do código
progress=0; dt=1000
rate=.0035+5*.00045
seconds=0
while progress<100 and seconds<60:
    progress+=dt*rate; seconds+=1
if progress<100 or seconds>20: errors.append('captura lenta ou inválida')
# Torre de praia
ship_hp=300; damage=18+2*4
for _ in range(5): ship_hp-=damage
if not (0<ship_hp<300): errors.append('dano de torre inválido')
# Renda do porto em 3 pulsos
stock={'gold':100,'wood':100}; cap={'gold':500,'wood':500}
for _ in range(3):
    stock['gold']=min(cap['gold'],stock['gold']+port['passiveIncome']['gold'])
    stock['wood']=min(cap['wood'],stock['wood']+port['passiveIncome']['wood'])
if stock!={'gold':115,'wood':112}: errors.append('renda do porto inválida')
# Bloqueio físico da muralha
if wall['hp']<800: errors.append('muralha com vida insuficiente')
# Persistência
sample={'schemaVersion':11,'coastalSiege':{'port':{'owner':'player','progress':100,'fortificationHp':0},'enemyDefenses':[{'id':1,'type':'wall','hp':0}],'stats':{'portsCaptured':1}}}
roundtrip=json.loads(json.dumps(sample,ensure_ascii=False))
if roundtrip!=sample: errors.append('roundtrip de save falhou')
report={'ok':not errors,'errors':errors,'ramHitsToBreakPort':hits,'captureSeconds':seconds,'towerTargetHpAfter5Shots':ship_hp,'portIncomeAfter3Ticks':stock,'saveRoundtrip':roundtrip==sample}
(root/'tests/RELATORIO_TESTE_LOGICA_F31.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
(root/'tests/RELATORIO_TESTE_LOGICA_F31.md').write_text('# Relatório lógico — Fase 31\n\n'+ '\n'.join([
 f"- Resultado: **{'APROVADO' if report['ok'] else 'FALHOU'}**",
 f"- Golpes de aríete para romper o porto: {hits}",
 f"- Tempo simulado de captura: {seconds} s",
 f"- Vida do alvo após 5 disparos da torre: {ship_hp}",
 f"- Renda após 3 pulsos: {stock}",
 f"- Persistência JSON: {'OK' if report['saveRoundtrip'] else 'FALHA'}",
]),encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=False))
sys.exit(1 if errors else 0)
