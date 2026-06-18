# Fase 19 — Animações de Unidades e Edifícios

## Estados de unidades
- idle: respiração e balanço leve;
- moving/engaging/patrolling: passos, inclinação e poeira;
- gathering: movimento de ferramenta;
- building/repairing: martelo animado;
- fighting: avanço e golpe;
- cavalry: passada mais rápida e sombra ampliada.

## Estados dos edifícios
- fundação: imagem semitransparente, andaimes, progresso e faíscas;
- concluído: pulsação mínima e detalhes vivos;
- moinho: pás rotativas;
- estruturas militares e posto avançado: bandeira animada;
- casas e estruturas econômicas: fumaça leve;
- danificado: vibração e fumaça escura.

## Acessibilidade e desempenho
O motor consulta:
- Movimento reduzido;
- modo seguro;
- qualidade visual “Desempenho”.

Nessas condições, o jogo mantém a leitura visual sem animações decorativas intensas.

## Evolução artística futura
O sistema foi preparado para receber spritesheets exclusivos com:
- oito direções;
- caminhada;
- coleta;
- construção;
- ataque;
- dano;
- morte.
