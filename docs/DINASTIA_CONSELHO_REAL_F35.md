# Fase 35 — Dinastia, Conselho Real e Eventos Políticos

## Objetivo

A Fase 35 transforma o governante escolhido pelo jogador em parte de uma dinastia persistente. O reino agora possui legitimidade política, sucessão, herdeiro, conselheiros e eventos internos.

## Sistemas

### Legitimidade

A legitimidade representa a aceitação do governante pelo reino. Ela é influenciada por decisões de corte, estabilidade social, conselheiros e eventos.

### Autoridade

A autoridade representa a capacidade do governante impor decisões. Ela é afetada por desfiles militares, leis de sucessão e crises.

### Apoios sociais

- Nobreza;
- Clero;
- Povo.

A média desses fatores define se o reino está estável, frágil ou em crise política.

## Conselheiros reais

- Chanceler;
- Marechal;
- Tesoureiro;
- Mestre de Espiões;
- Mordomo-Mor.

Conselheiros reduzem instabilidade e fortalecem o reino por influência.

## Leis de sucessão

- Primogenitura;
- Monarquia Eletiva;
- Sucessão por Mérito.

Cada lei altera legitimidade, autoridade e apoio da nobreza/povo.

## Decisões políticas

As decisões consomem recursos reais da partida quando o jogo está ativo.

- Realizar Corte: custa ouro e melhora legitimidade;
- Banquete Real: custa alimento e ouro e melhora apoio popular;
- Desfile Militar: custa ouro e madeira e melhora autoridade;
- Codificar Sucessão: custa ouro e pedra e estabiliza a sucessão.

## Persistência

O sistema é salvo em:

- `localStorage: valeEmpires.royalPolitics`;
- campo `royalPolitics` dentro do save principal.

## Anti-quebra

Se o sistema externo não estiver carregado, o jogo principal continua funcionando. Se um save antigo não tiver dados políticos, o Conselho Real cria uma dinastia segura automaticamente.
