# Partida Livre — Fase 25

## Arquitetura

O estado global passou a distinguir:

```text
gameMode: campaign | skirmish
```

A configuração da escaramuça é normalizada antes de iniciar ou restaurar a partida.

## Configuração persistente

A chave `valeEmpires.skirmish` armazena as preferências da tela de configuração:

```json
{
  "mapSize": "standard",
  "startingEra": 0,
  "resources": "standard",
  "victory": "conquest",
  "difficulty": "normal",
  "seed": 123456
}
```

## Save schema 5

O save registra:

```json
{
  "schemaVersion": 5,
  "gameMode": "skirmish",
  "skirmish": {},
  "skirmishRuntime": {},
  "eraPack": "medieval"
}
```

Os slots dedicados impedem que uma escaramuça apague silenciosamente o último estado salvo da campanha.

## Geração de mapa

O gerador procedural existente foi mantido. Apenas as dimensões mudam conforme o preset:

- Compacto: 40 × 40 tiles;
- Padrão: 56 × 56 tiles;
- Grande: 72 × 72 tiles.

A mesma semente e o mesmo tamanho produzem a mesma base procedural.

## Reutilização segura

A Partida Livre reutiliza sistemas já auditados:

- perfil do governante;
- civilizações e bônus;
- eras e tecnologias;
- IA adaptativa;
- combate e pathfinding;
- neblina, território e pontos estratégicos;
- áudio, animações, acessibilidade e PWA.

O progresso oficial da campanha permanece fora da lógica de vitória da escaramuça.
