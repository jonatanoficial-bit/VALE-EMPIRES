# Relatório de Teste Automatizado — Fase 11

## Ambiente simulado
- resolução: 915 × 412 px;
- orientação: horizontal;
- entrada: toque;
- armazenamento local e canvas simulados;
- inicialização completa do JavaScript dentro de ambiente isolado.

## Teste 1 — Nova campanha
- [x] menu principal inicializou;
- [x] modo de recuperação permaneceu oculto;
- [x] criação de governante abriu;
- [x] campanha iniciou;
- [x] HUD exibiu Era Tribal;
- [x] Arqueiro e Cavalaria apareceram bloqueados;
- [x] Casa permaneceu desbloqueada;
- [x] painel de eras abriu mostrando a Era Feudal.

## Teste 2 — Restauração de save
- [x] save na Era dos Reinos foi carregado;
- [x] HUD restaurou Era dos Reinos;
- [x] Arqueiro, Cavalaria e Estábulo foram desbloqueados;
- [x] painel indicou Era Imperial como próximo avanço;
- [x] modo de recuperação permaneceu oculto.

## Integridade
- [x] sintaxe JavaScript validada por `node --check`;
- [x] referências locais do HTML verificadas;
- [x] pacote ZIP testado após geração.
