# Roteiro de Teste — Fase 25

## Menu e perfil

1. Abrir o jogo em celular horizontal.
2. Confirmar que **Partida Livre** aparece no menu.
3. Tocar no botão e confirmar o período Medieval.
4. Criar ou confirmar governante, avatar e civilização.
5. Confirmar que a tela de configuração abre sem Modo de Recuperação.

## Configuração

1. Alternar entre os três tamanhos de mapa.
2. Alternar entre as quatro eras iniciais.
3. Alternar recursos, dificuldade e condição de vitória.
4. Informar uma semente numérica.
5. Iniciar a partida e verificar se HUD, mapa e unidades carregam.

## Condições de vitória

- Conquista: confirmar contagem de abates e inimigos ativos.
- Dominação: controlar quatro pontos e acompanhar os 120 segundos.
- Supremacia: alcançar os três requisitos exibidos no painel.

## Persistência

1. Salvar uma campanha.
2. Iniciar e salvar uma Partida Livre.
3. Confirmar a presença dos slots `valeEmpires.save.campaign` e `valeEmpires.save.skirmish`.
4. Usar Continuar e confirmar a restauração do último modo.
5. Exportar e importar o save.

## Dispositivos

Testar ao menos:

- Android 915×412 ou equivalente;
- Android pequeno em paisagem;
- iPhone em paisagem;
- desktop 1366×768;
- PWA instalada e navegador normal.
