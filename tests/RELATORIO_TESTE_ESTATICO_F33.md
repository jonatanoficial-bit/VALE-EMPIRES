# Relatório Estático — Fase 33

- Build: **VE-3.9.0-F33**
- IDs HTML: **278**
- IDs duplicados: **0**
- Referências HTML: **138**
- JSONs validados: **49**
- Resultado: **APROVADO**

Todos os JavaScripts e o service worker passaram em `node --check`. O servidor HTTP local respondeu corretamente para `index.html`, `js/app.js` e `data/urban/city-administration.json`.

O Chromium headless não concluiu dentro de 25 segundos por restrições de DBus, NETLINK e inotify do ambiente. Isso não foi contado como aprovação de execução real.
