# Changelog — Vale Empires

## v4.13.0 — Fase 47 — Tema Musical Oficial e Áudio Premium

- Inserido o MP3 instrumental enviado pelo usuário como tema oficial do jogo.
- Atualizado `js/audio-engine.js` para usar o novo tema no menu, exploração e jogo principal.
- Ajustada a troca de cenas para não reiniciar a mesma faixa quando o caminho de áudio é igual.
- Atualizado `assets/audio/audio-manifest.json` com metadados do tema oficial.
- Atualizado `service-worker.js` com cache novo e inclusão do MP3 no pacote PWA.
- Mantidos os áudios antigos como legado/fallback interno no pacote, sem serem a trilha principal.
- Ampliado diagnóstico de storage para incluir Justiça e Demografia.
- Preservadas as Fases 1–46.
