from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
import json, re, sys, math, heapq
root=Path(__file__).resolve().parents[1]
errors=[]
app=(root/'js/app.js').read_text(encoding='utf-8')
html=(root/'index.html').read_text(encoding='utf-8')
checks=[
 ('schema 8+','schemaVersion:9' in app or 'schemaVersion:8' in app),
 ('naval state','navalWorld:null' in app and 'ships:[]' in app),
 ('harbor building',"harbor:{label:'Porto Real'" in app),
 ('coastal validation',"type==='harbor'||type==='shipyard'" in app or "type==='harbor'&&!hasAdjacentWater" in app),
 ('water pathfinding','function findWaterPath' in app),
 ('naval update','function updateNavalWorld' in app and 'updateNavalWorld(dt)' in app),
 ('naval rendering','drawNavalRoutes();' in app and 'drawShips();' in app),
 ('naval save','navalWorld:serializeNavalWorld()' in app),
 ('naval restore','initializeNavalWorld(s.navalWorld)' in app),
 ('harbor button','data-building="harbor"' in html),
 ('naval stats','id="navalShipsStat"' in html),
]
for name,ok in checks:
 if not ok: errors.append(name)
# DOM duplicate check
soup=BeautifulSoup(html,'html.parser')
ids=[x.get('id') for x in soup.find_all(attrs={'id':True})]
dups=[k for k,v in Counter(ids).items() if v>1]
if dups: errors.append(f'duplicate ids {dups}')
# Water-route logic simulation matching the map foundation
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
  x=channel_x+dx
  if 0<=x<cols: water.add((x,y))
start=(5,sea_start+2); goal=(25,river[25]+1)
def astar(a,b):
 q=[(0,a)]; g={a:0}; parent={}
 while q:
  _,cur=heapq.heappop(q)
  if cur==b:
   path=[]
   while cur!=a:path.append(cur);cur=parent[cur]
   return list(reversed(path))
  for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
   n=(cur[0]+dx,cur[1]+dy)
   if n not in water: continue
   ng=g[cur]+(1.414 if dx and dy else 1)
   if ng<g.get(n,1e9):
    g[n]=ng;parent[n]=cur
    h=max(abs(n[0]-b[0]),abs(n[1]-b[1]))
    heapq.heappush(q,(ng+h,n))
 return None
route=astar(start,goal)
if not route: errors.append('water route not connected')
# Data files
build=json.loads((root/'BUILD.json').read_text(encoding='utf-8'))
if int(build.get('saveSchema',0))<8: errors.append('BUILD saveSchema')
naval=json.loads((root/'data/naval/maritime-trade.json').read_text(encoding='utf-8'))
if sum(naval['cargo']['trade'].values())!=34: errors.append('trade cargo total')
if sum(naval['cargo']['alliance'].values())!=58: errors.append('alliance cargo total')
report={'ok':not errors,'errors':errors,'html_ids':len(ids),'water_route_nodes':len(route or []),'trade_cargo_total':34,'alliance_cargo_total':58}
(root/'tests/RELATORIO_TESTE_LOGICA_F28.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=False))
sys.exit(1 if errors else 0)
