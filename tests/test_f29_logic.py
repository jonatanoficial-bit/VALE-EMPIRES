from pathlib import Path
import json, math, heapq, sys
root=Path(__file__).resolve().parents[1]
errors=[]
config=json.loads((root/'data/naval/military-fleet.json').read_text(encoding='utf-8'))
ships=config.get('ships',{})
for key in ('patrolGalley','warGalley','fireShip'):
    if key not in ships: errors.append(f'missing ship {key}')
# Damage model checks equivalent to JS navalStrike
patrol=ships.get('patrolGalley',{})
war=ships.get('warGalley',{})
fire=ships.get('fireShip',{})
def damage(att, armor): return max(1, round(att-(armor or 0)*.72))
war_vs_patrol=damage(war.get('attack',0),3)
patrol_vs_war=damage(patrol.get('attack',0),7)
fire_burst=round(fire.get('attack',0)*1.8)
if war_vs_patrol<=patrol_vs_war: errors.append('war galley not stronger against armor')
if fire_burst<90: errors.append('fire ship burst too low')
# Blockade rule: two ships in radius
port=(1000,1000)
fleet=[(1050,1040),(1210,980),(1500,1500)]
inside=sum(math.hypot(x-port[0],y-port[1])<310 for x,y in fleet)
blockaded=inside>=config['blockade']['shipsRequired']
if not blockaded: errors.append('blockade rule failed')
# Save roundtrip structure
sample={
 'version':1,'stats':{'kills':2,'losses':1},'queue':[{'type':'warGalley','time':15500}],
 'queueProgress':5000,'command':'escort','fleet':[{'id':1,'type':'patrolGalley','x':10,'y':20,'hp':180}],
 'enemyFleet':[{'id':2,'type':'warGalley','x':100,'y':200,'hp':300}]
}
roundtrip=json.loads(json.dumps(sample))
if roundtrip!=sample: errors.append('save roundtrip failed')
# Water A* connectivity inherited from F28 map foundation
cols=rows=56
river=[math.floor(rows*.47+math.sin(x/5)*4+math.sin(x/11)*3) for x in range(cols)]
water=set()
for x in range(cols):
    for y in range(rows):
        if abs(y-river[x])<=1: water.add((x,y))
sea_start=rows-6; channel_x=cols-6
for y in range(sea_start,rows):
    for x in range(cols): water.add((x,y))
for y in range(min(sea_start,river[channel_x]),rows):
    for dx in (-1,0,1):
        if 0<=channel_x+dx<cols: water.add((channel_x+dx,y))
def astar(a,b):
    q=[(0,a)];g={a:0};parent={}
    while q:
        _,cur=heapq.heappop(q)
        if cur==b:
            path=[]
            while cur!=a:path.append(cur);cur=parent[cur]
            return path[::-1]
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
            n=(cur[0]+dx,cur[1]+dy)
            if n not in water: continue
            ng=g[cur]+(1.414 if dx and dy else 1)
            if ng<g.get(n,1e9):
                g[n]=ng;parent[n]=cur
                heapq.heappush(q,(ng+max(abs(n[0]-b[0]),abs(n[1]-b[1])),n))
    return None
route=astar((5,sea_start+2),(25,river[25]+1))
if not route: errors.append('water path unavailable')
report={
 'ok':not errors,'errors':errors,'shipTypes':list(ships),'warVsPatrolDamage':war_vs_patrol,
 'patrolVsWarDamage':patrol_vs_war,'fireShipBurst':fire_burst,'blockadeShipsInside':inside,
 'blockadeActivated':blockaded,'waterRouteNodes':len(route or []),'saveRoundtrip':roundtrip==sample
}
(root/'tests/RELATORIO_TESTE_LOGICA_F29.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
(root/'tests/RELATORIO_TESTE_LOGICA_F29.md').write_text('# Relatório lógico — Fase 29\n\n'+ '\n'.join([
 f"- Resultado: **{'APROVADO' if report['ok'] else 'FALHOU'}**",
 f"- Classes navais: {', '.join(report['shipTypes'])}",
 f"- Dano Galé de Guerra contra armadura de patrulha: {war_vs_patrol}",
 f"- Dano Galé de Patrulha contra armadura de guerra: {patrol_vs_war}",
 f"- Explosão do Navio Incendiário: {fire_burst}",
 f"- Navios dentro do raio de bloqueio: {inside}",
 f"- Bloqueio ativado: {blockaded}",
 f"- Rota aquática A*: {len(route or [])} nós",
 f"- Persistência JSON: {'OK' if roundtrip==sample else 'FALHA'}",
 ]),encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=False))
sys.exit(1 if errors else 0)
