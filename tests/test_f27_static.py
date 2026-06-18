from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[1]
app=(root/'js/app.js').read_text(encoding='utf-8')
build=json.loads((root/'BUILD.json').read_text(encoding='utf-8'))
checks={
 'build v3.3.0': build.get('version')=='v3.3.0',
 'fase 27': build.get('phase')=='27',
 'schema 7': build.get('saveSchema')==7 and 'schemaVersion:7' in app,
 'entrepostos': 'defaultTradeWorld' in app and 'drawFactionEnclaves' in app,
 'rotas físicas': 'drawTradeRoutes' in app and 'ensureTradeRoute' in app,
 'caravanas': 'spawnTradeCaravan' in app and 'drawCaravans' in app,
 'entrega': 'deliverCaravan' in app and 'tradeCargoFor' in app,
 'saque': 'caravanRaid' in app and 'raider.state' in app,
 'save comércio': 'tradeWorld:serializeTradeWorld()' in app and 'initializeTradeWorld(s.tradeWorld)' in app,
 'dados': (root/'data/trade/physical-routes.json').exists(),
 'pwa': 'data/trade/physical-routes.json' in (root/'service-worker.js').read_text(encoding='utf-8'),
}
for name,ok in checks.items(): print(('OK' if ok else 'FAIL'),name)
if not all(checks.values()): sys.exit(1)
