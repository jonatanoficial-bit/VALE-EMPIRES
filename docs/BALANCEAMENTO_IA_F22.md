# Fase 22 — Balanceamento e Inteligência Artificial Final

## Perfis

### História
Foco narrativo. Jogador recebe recursos e força extras; a IA cresce lentamente e ataca com menos frequência.

### Fácil
Pressão moderada, boa margem para aprender economia e combate.

### Normal
Referência principal de balanceamento e experiência recomendada.

### Difícil
IA cresce e produz mais rapidamente, adapta a composição do exército e envia ondas maiores.

### Conquistador
Pressão máxima, contra-unidades frequentes, pouca retirada e maior recompensa.

## Diretor adaptativo
O diretor monitora a proporção entre exército inimigo e exército do jogador. Ele alterna entre:
- recuperação;
- equilíbrio;
- pressão.

O sistema não concede vitória automática. Ele regula frequência de ataques, produção e comportamento anti-estagnação dentro dos multiplicadores da dificuldade escolhida.

## Compatibilidade
Saves sem campo `difficulty` recebem `normal`. O pacote medieval continua isolado dos pacotes multiera bloqueados.
