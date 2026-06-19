# Fase 47 — Tema Musical Oficial e Áudio Premium

Build: `VE-4.13.0-F47-TEMA-MUSICAL-OFICIAL-AUDIO-PREMIUM`  
Versão: `v4.13.0`

## Objetivo

Substituir a música simples anterior por um tema instrumental oficial enviado pelo usuário, deixando a identidade sonora do Vale Empires mais forte e adequada para uma build comercial.

## Implementação

- MP3 original recebido: `Vale empires tema.mp3`.
- Caminho final no jogo: `assets/audio/music/vale-empires-official-theme.mp3`.
- Usado como trilha principal em:
  - menu;
  - exploração;
  - partida principal;
  - combate, sem troca brusca para a trilha simples anterior.

## Compatibilidade

O áudio continua respeitando a exigência dos navegadores mobile: a música começa após o primeiro toque/clique do jogador. Os controles de volume existentes continuam funcionando na tela de configurações.

## PWA/cache

O Service Worker foi atualizado para `vale-empires-v4.13.0-f47-official-theme-audio`, forçando o navegador a baixar a nova trilha após o deploy.
