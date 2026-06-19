# Fase 42 — Infraestrutura imperial, logística profunda e obras públicas

## Objetivo

Transformar o Vale Empires em um simulador estratégico mais profundo, onde o jogador precisa manter o reino fisicamente conectado. A economia, o abastecimento, a mobilidade militar e a estabilidade provincial passam a depender da rede de estradas, pontes, depósitos, correios, torres de sinal e corredores regionais.

## Sistemas incluídos

- Eficiência logística geral.
- Estradas reais.
- Pontes e travessias.
- Depósitos regionais.
- Correios imperiais.
- Torres de sinal e vigia.
- Anel logístico da capital.
- Corredores regionais com condição, fluxo, ameaça e guarnição.
- Gargalos logísticos.
- Banditismo em rotas.
- Manutenção e desgaste.
- Mobilidade militar.
- Integração regional.
- Apoio popular às obras públicas.

## Integrações

- `ValeInternalEconomy.score()` influencia a capacidade logística.
- `ValeReligionCivilization.identity()` influencia o apoio às obras.
- `ValeEmpiresAPI.getSnapshot()` fornece recursos, armazenamento e coesão provincial.
- `ValeEmpiresAPI.spend()` consome recursos reais do jogador.
- `ValeEmpiresAPI.addStock()` devolve ganhos de fluxo logístico quando aplicável.

## Persistência

Campo do save: `imperialLogistics`  
Schema do save: `22`

## Anti-quebra

O módulo usa carregamento isolado, overlay dinâmico, optional chaining e checagem de botão ausente. Caso o painel não esteja disponível, o restante do jogo continua funcionando.
