# VALE EMPIRES — Manifesto de Assets — Fase 01

**Build:** VE-0.1.0-F01  
**Quantidade de arquivos PNG:** 29  

## Estrutura e caminhos

### Branding
- `assets/branding/vale-empires-logo-fullscreen.png` — 1672×941 px

### Fundos
- `assets/backgrounds/loading-screen-background-alternative.png` — 1672×941 px
- `assets/backgrounds/loading-screen-background.png` — 1672×941 px
- `assets/backgrounds/menu-main-background.png` — 1672×941 px

### Painéis de interface
- `assets/ui/panels/medieval-premium-interface.png` — 1672×941 px
- `assets/ui/panels/panel-large-torch.png` — 890×475 px
- `assets/ui/panels/panel-wide-dark.png` — 830×165 px
- `assets/ui/panels/panel-wide-parchment.png` — 855×240 px

### Botões
- `assets/ui/buttons/button-back.png` — 183×51 px
- `assets/ui/buttons/button-continue.png` — 423×63 px
- `assets/ui/buttons/button-credits.png` — 423×62 px
- `assets/ui/buttons/button-new-game.png` — 440×92 px
- `assets/ui/buttons/button-restart.png` — 179×55 px
- `assets/ui/buttons/button-safe-mode.png` — 215×57 px
- `assets/ui/buttons/button-settings.png` — 423×61 px

### Ícones
- `assets/ui/icons/build-badge-ve-0.1.0-f01.png` — 1536×1024 px
- `assets/ui/icons/icon-close.png` — 91×96 px
- `assets/ui/icons/icon-scroll.png` — 87×91 px
- `assets/ui/icons/icon-settings.png` — 81×85 px
- `assets/ui/icons/icon-shield.png` — 86×92 px

### Terrenos separados
- `assets/terrain/terrain-dirt.png` — 512×512 px
- `assets/terrain/terrain-grass-dark.png` — 512×512 px
- `assets/terrain/terrain-grass-light.png` — 512×512 px
- `assets/terrain/terrain-rock.png` — 512×512 px
- `assets/terrain/terrain-stone-path.png` — 512×512 px
- `assets/terrain/terrain-water-shallow.png` — 512×512 px

### Placeholder
- `assets/placeholders/test-placeholder-emblem.png` — 1254×1254 px

### Imagens-fonte compostas
- `assets/source-sheets/terrain-source-sheet.png` — 1254×1254 px
- `assets/source-sheets/ui-buttons-source-sheet.png` — 1536×1024 px

## Observações de integração

- As seis texturas do terreno foram recortadas da prancha original e padronizadas em **512×512 px**.
- Os botões e ícones foram recortados individualmente da imagem composta para facilitar a integração no jogo.
- As imagens compostas originais foram preservadas em `assets/source-sheets/` para auditoria e novos recortes.
- Para carregamento no Phaser, utilize os caminhos relativos exatamente como aparecem neste documento.
- Alguns botões contêm o texto renderizado na própria imagem. Para tradução futura, recomenda-se usar versões sem texto e aplicar o rótulo pelo HTML/Phaser.

## Exemplo de carregamento no Phaser

```javascript
this.load.image('menuBackground', 'assets/backgrounds/menu-main-background.png');
this.load.image('buttonNewGame', 'assets/ui/buttons/button-new-game.png');
this.load.image('terrainGrassLight', 'assets/terrain/terrain-grass-light.png');
```
