# Fase 31 — Cerco Costeiro e Conquista de Portos

## Muralha Costeira
Edifício da Era Feudal que bloqueia passagens de praia e força invasores a procurar rotas alternativas ou destruí-la.

## Torre de Praia
Defesa automática contra tropas desembarcadas, transportes, corsários e navios militares próximos.

## Oficina de Cerco
Edifício da Era dos Reinos necessário para produzir Aríetes de Cerco.

## Aríete de Cerco
Unidade lenta e resistente, com grande bônus contra muralhas, torres, fortificações e portos. Pode ser embarcada em transportes anfíbios.

## Porto rival
O porto possui:
- fortificação de 950 pontos;
- muralhas e torres próprias;
- zona de captura;
- progresso de ocupação de 0 a 100%;
- possibilidade de retomada pela IA.

Quando conquistado:
- interrompe reforços navais rivais;
- concede recompensa inicial de 200 de ouro;
- gera pequena renda periódica de madeira e ouro;
- aparece como conquistado no mapa e no minimapa.

## Save schema 11
O objeto `coastalSiege` preserva:
- dono e progresso do porto;
- vida da fortificação;
- defesas rivais restantes;
- estatísticas de cerco;
- temporizadores de captura e contra-ataque.
