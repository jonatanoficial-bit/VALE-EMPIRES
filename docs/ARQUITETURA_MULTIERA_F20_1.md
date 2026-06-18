# Arquitetura Multiera — Fase 20.1

## Princípio anti-quebra
Cada período é tratado como um pacote independente. Um pacote incompleto não pode iniciar uma partida. A campanha medieval nunca busca unidades, recursos ou tecnologias contemporâneas.

## Pacotes
- `medieval`: jogável.
- `renaissance`: planejado e bloqueado.
- `industrial`: planejado e bloqueado.
- `early-1900s`: planejado e bloqueado.
- `modern`: planejado e bloqueado.

## Save
O save versão 4 armazena `eraPack`. Saves antigos recebem automaticamente `medieval`. Caso um ID desconhecido seja encontrado, o sistema aplica fallback para Medieval.

## Expansão moderna
O cadastro preliminar contém Brasil, Estados Unidos, China, Índia, Japão, Alemanha, França, Reino Unido, Turquia, México, África do Sul e Rússia. Esses registros não representam conteúdo jogável nesta fase.

## Caminho até o produto final
A versão Medieval deve chegar ao release comercial antes de ativarmos o pacote Moderno. Isso permite vender um jogo completo e depois lançar a expansão com qualidade equivalente, sem comprometer estabilidade ou identidade histórica.
