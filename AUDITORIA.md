# Auditoria — Fase 36

## Escopo auditado

- JavaScript da aplicação;
- novo `court-intrigue.js`;
- `royal-politics.js`;
- `release-guard.js`;
- `service-worker.js`;
- HTML e referências locais;
- JSONs;
- manifesto SHA-256;
- ZIP final.

## Resultado

- [x] Função `centerCamera()` preservada;
- [x] `btnCourtIntriguePanel` presente no HTML;
- [x] `court-intrigue.js` incluído no HTML e no cache PWA;
- [x] save principal atualizado para schema 16;
- [x] campo `courtIntrigue` serializado e restaurado;
- [x] migração defensiva no release guard;
- [x] sintaxe JavaScript validada;
- [x] JSONs validados;
- [x] ZIP validado sem corrupção.

## Observação

O navegador Chromium headless pode falhar no ambiente por restrições administrativas. Fullscreen, toque, áudio e PWA instalada devem ser confirmados em dispositivos reais.
