# Relatório de Teste Automatizado — Fase 17

## Ambiente simulado
- viewport: 915 × 412 px;
- orientação: horizontal;
- navegador: Chromium headless;
- armazenamento local simulado para validar perfil, save e backup;
- preload de imagens neutralizado apenas no teste automatizado para evitar dependência de rede do sandbox.

## Fluxo validado
- [x] loading conclui e abre o menu;
- [x] configurações abrem sem erro;
- [x] controles de acessibilidade são renderizados;
- [x] alto contraste é aplicado ao `body`;
- [x] saúde do save é exibida;
- [x] Novo Jogo abre a criação do governante;
- [x] nome, avatar e nação podem ser selecionados;
- [x] mapa da campanha abre;
- [x] missão inicial abre a partida;
- [x] save principal é criado;
- [x] segundo save cria backup automático;
- [x] horário do último save é gravado;
- [x] perfil é persistido;
- [x] nenhum erro JavaScript foi capturado nos fluxos simulados.

## PWA
Manifesto, service worker, ícones e tela offline foram validados estruturalmente. A instalação real e o cache offline devem ser confirmados após publicação em HTTPS, pois o sandbox bloqueia navegação para origens locais durante o teste automatizado.
