# Fase 27 — Facções, Caravanas e Rotas Comerciais

## Representação das facções
Cada civilização estrangeira não rival recebe um entreposto físico gerado em terreno transitável, afastado do Centro Urbano, da base rival e de outros entrepostos.

## Rotas
Ao assinar Comércio ou Aliança, o jogo calcula uma rota A* do entreposto ao Centro Urbano. A rota é desenhada no mapa depois que o entreposto é explorado.

## Caravanas
- Comércio: 6 alimento e 12 ouro; despacho a cada 30 segundos.
- Aliança: 10 madeira, 10 alimento, 10 ouro e 4 pedra; despacho a cada 22 segundos.
- A carga só entra no estoque ao chegar ao Centro Urbano.
- A caravana retorna ao entreposto depois da entrega.

## Risco
Patrulhas do rival ativo podem atacar caravanas de saída. Uma perda reduz relação e confiança com a corte proprietária.

## Save schema 7
O save registra `tradeWorld`, incluindo posições dos entrepostos, contadores de entregas/perdas e caravanas em trânsito. Rotas A* são recalculadas ao carregar para evitar persistir dados obsoletos.
