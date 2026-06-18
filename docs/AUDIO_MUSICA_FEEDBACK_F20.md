# Sistema de Áudio — Fase 20

## Arquitetura

O sistema está isolado em:

`js/audio-engine.js`

A API global utilizada pelo jogo é:

- `VALE_AUDIO.unlock()`
- `VALE_AUDIO.setScene(scene)`
- `VALE_AUDIO.setCombat(active)`
- `VALE_AUDIO.playMusic(key)`
- `VALE_AUDIO.playSfx(key, options)`
- `VALE_AUDIO.playNationStinger(id)`
- `VALE_AUDIO.playResult(victory)`
- `VALE_AUDIO.duck(active)`
- `VALE_AUDIO.getPrefs()`
- `VALE_AUDIO.diagnostics()`

## Caminhos das músicas

- `assets/audio/music/menu-royal.ogg`
- `assets/audio/music/exploration-fields.ogg`
- `assets/audio/music/combat-siege.ogg`
- `assets/audio/music/victory-fanfare.ogg`
- `assets/audio/music/defeat-lament.ogg`

## Vinhetas de civilização

- `assets/audio/stingers/nation-england.ogg`
- `assets/audio/stingers/nation-france.ogg`
- `assets/audio/stingers/nation-byzantium.ogg`
- `assets/audio/stingers/nation-mongol.ogg`
- `assets/audio/stingers/nation-cordoba.ogg`
- `assets/audio/stingers/nation-norse.ogg`

## Efeitos principais

A pasta `assets/audio/sfx/` contém efeitos para:

- interface;
- confirmação e erro;
- seleção e movimento;
- madeira, alimento, ouro e pedra;
- construção e reparo;
- espada, flecha, cavalaria e impacto;
- morte de unidade;
- edifício concluído;
- avanço de era;
- tecnologia concluída;
- captura territorial;
- autosave e notificação.

## Mixagem

As preferências ficam em:

`localStorage['valeEmpires.audioPrefs']`

Estrutura:

```json
{
  "master": 0.85,
  "music": 0.55,
  "sfx": 0.78,
  "ui": 0.68,
  "muted": false,
  "dynamic": true
}
```

## Música dinâmica

- menu, perfil e mapa de campanha usam `menu-royal`;
- partida normal usa `exploration-fields`;
- combate ativo muda para `combat-siege`;
- após aproximadamente 3,5 segundos sem combate, a exploração retorna;
- vitória e derrota interrompem temporariamente a trilha e depois restauram a cena.

## Política de autoplay

Navegadores mobile exigem interação do usuário. O motor é liberado no primeiro toque, clique ou comando do usuário. Antes disso, a build permanece totalmente funcional em silêncio.

## Substituição futura

Novas músicas masterizadas podem substituir os arquivos mantendo os mesmos nomes e caminhos. O código não precisará ser reescrito.
