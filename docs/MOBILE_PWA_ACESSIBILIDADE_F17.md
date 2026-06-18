# Mobile, PWA e Acessibilidade — Fase 17

## PWA
A build inclui `manifest.webmanifest`, `service-worker.js`, ícones e tela offline. O service worker usa cache do shell e cache progressivo dos arquivos utilizados. A instalação requer HTTPS.

## Autosave e recuperação
- intervalo padrão: 60 segundos;
- eventos extras: troca de tela, ocultação da página e `pagehide`;
- save anterior armazenado em `valeEmpires.save.backup`;
- exportação e importação em JSON;
- restauração manual no painel de configurações.

## Acessibilidade
Preferências persistentes:
- alto contraste;
- movimento reduzido;
- interface ampliada;
- escala de 100% a 130%;
- paleta alternativa para diferenciação de equipes;
- vibração tátil opcional.

## Mobile
- orientação paisagem;
- fullscreen quando permitido;
- safe-area para notch;
- controles por toque e pinça;
- wake lock quando disponível;
- alvos de toque mínimos para telas touch.
