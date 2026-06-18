# Sistema de Eras — Fase 11

## Ordem atual
1. Era Tribal
2. Era Feudal
3. Era dos Reinos
4. Era Imperial

## Desbloqueios principais
- Tribal: economia inicial, quartel e infantaria.
- Feudal: campo de arqueiros e arqueiros.
- Reinos: estábulo e cavalaria.
- Imperial: bônus máximos econômicos, militares e estruturais.

## Persistência
O save contém `eraIndex`, `eraResearch` e `eraHistory`. A IA mantém seus próprios campos de era dentro de `enemyAI`.

## Expansões futuras
A arquitetura aceita novos registros em `ERA_DEFS`. Estão planejados, sem implementação nesta build:
- Renascimento e Grandes Navegações;
- Era Industrial;
- início dos anos 1900;
- mundo contemporâneo.

Cada expansão poderá fornecer novos assets, edifícios, unidades, tecnologias e campanhas sem alterar saves medievais existentes.
