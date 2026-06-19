# Fase 43 — Saúde Pública, Saneamento e Bem-estar Popular

Build: **VE-4.9.0-F43-PUBLIC-HEALTH**  
Versão: **v4.9.0**  
Schema de save: **23**

## Objetivo

Esta fase adiciona uma camada profunda de saúde pública ao Vale Empires. O reino passa a ter saneamento, água potável, enfermarias, curandeiros, segurança alimentar, medicina, vigilância de doenças, quarentena, risco epidêmico e bem-estar popular.

## Sistemas adicionados

- Painel HUD **Saúde Pública** (`btnPublicHealthPanel`).
- Módulo `js/public-health.js` com overlay próprio anti-quebra.
- Dados estratégicos em `data/society/public-health.json`.
- Persistência no save principal pelo campo `publicHealth`.
- Integração com `ValeImperialLogistics`, `ValeInternalEconomy` e `ValeReligionCivilization`.
- Exportação de dossiê JSON.

## Redes sanitárias

1. Poços e cisternas.
2. Limpeza das ruas.
3. Enfermarias reais.
4. Guilda dos curandeiros.
5. Inspeção de mercados.
6. Casas de quarentena.

## Distritos sanitários

- Capital.
- Distrito do rio.
- Bairro do mercado.
- Quartel e muralhas.
- Aldeias próximas.

## Doutrinas sanitárias

- Prevenção comunitária.
- Quarentena de emergência.
- Hospitais cívico-religiosos.
- Medicina das guildas.

## Medidas jogáveis

- Abrir poços protegidos.
- Limpar ruas e canais.
- Erguer enfermaria real.
- Treinar curandeiros e parteiras.
- Inspecionar feiras e celeiros.
- Criar cordão sanitário.

## Anti-quebra

O módulo cria o overlay dinamicamente, ignora botões ausentes com segurança, usa optional chaining para integração e mantém dados locais normalizados antes de salvar/restaurar.
