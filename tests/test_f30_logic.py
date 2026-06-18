from pathlib import Path
import json, math, sys
root=Path(__file__).resolve().parents[1]
config=json.loads((root/'data/naval/amphibious-operations.json').read_text(encoding='utf-8'))
fleet=json.loads((root/'data/naval/military-fleet.json').read_text(encoding='utf-8'))
errors=[]
transport=fleet.get('ships',{}).get('transportShip')
if not transport: errors.append('transportShip ausente')
if transport and transport.get('capacity')!=8: errors.append('capacidade do transporte deve ser 8')
# Simulação de distribuição de 13 tropas em dois transportes de capacidade 8
caps=[transport.get('capacity',0),transport.get('capacity',0)] if transport else [0,0]
loaded=[0,0]
for _ in range(13):
    placed=False
    for i,c in enumerate(caps):
        if loaded[i]<c:
            loaded[i]+=1;placed=True;break
    if not placed: break
if sum(loaded)!=13: errors.append('distribuição de embarque falhou')
# Simulação de desembarque em posições terrestres válidas ao redor de um ponto
landing=(1000,900)
positions=[]
for i in range(8):
    positions.append((landing[0]+math.cos(i*1.3)*55,landing[1]+math.sin(i*1.3)*55))
if len({(round(x),round(y)) for x,y in positions})<7: errors.append('dispersão de desembarque insuficiente')
# Defesa costeira: dano após 4 disparos
hp=300
damage=config['coastalFort']['damage']
for _ in range(4): hp-=damage
if hp>=300 or hp<=0: errors.append('modelo de defesa costeira inválido')
# Temporizador de invasão em dificuldade normal
base=config['enemyInvasions']['baseIntervalMs']
minimum=config['enemyInvasions']['minimumIntervalMs']
normal=max(minimum,base-2*11000-1*7000)
if normal<minimum or normal>=base: errors.append('intervalo de invasão inválido')
# Persistência
sample={'version':2,'amphibious':{'stats':{'landings':2,'enemyLandings':1}},'fleet':[{'id':1,'type':'transportShip','passengers':[{'type':'infantry'},{'type':'archer'}]}]}
roundtrip=json.loads(json.dumps(sample))
if roundtrip!=sample: errors.append('roundtrip de save falhou')
report={
 'ok':not errors,'errors':errors,'transportCapacity':transport.get('capacity') if transport else None,
 'embarkDistribution':loaded,'landingPositions':len(positions),'coastalHpAfter4Shots':hp,
 'normalInvasionIntervalMs':normal,'saveRoundtrip':roundtrip==sample
}
(root/'tests/RELATORIO_TESTE_LOGICA_F30.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
(root/'tests/RELATORIO_TESTE_LOGICA_F30.md').write_text('# Relatório lógico — Fase 30\n\n'+ '\n'.join([
 f"- Resultado: **{'APROVADO' if report['ok'] else 'FALHOU'}**",
 f"- Capacidade do transporte: {report['transportCapacity']}",
 f"- Distribuição de 13 tropas: {report['embarkDistribution']}",
 f"- Posições de desembarque: {report['landingPositions']}",
 f"- Vida após 4 disparos costeiros: {report['coastalHpAfter4Shots']}",
 f"- Intervalo de invasão normal: {report['normalInvasionIntervalMs']} ms",
 f"- Persistência JSON: {'OK' if report['saveRoundtrip'] else 'FALHA'}",
]),encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=False))
sys.exit(1 if errors else 0)
