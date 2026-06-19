# Hotfix Recuperação — Fase 40 v4.6.1

## Correção aplicada

A build v4.6.0 podia abrir o modo de recuperação com o erro:

```text
TypeError: Cannot read properties of null (reading 'classList')
```

A causa era a função `show()` tentando alternar a classe `active` em uma tela opcional ausente no HTML (`skirmishScreen`).

## Solução

- `show()` agora verifica `if(!e)return` antes de usar `classList`.
- Quando uma tela solicitada não existe, a build retorna ao menu com segurança.
- O cache do service worker foi alterado para `vale-empires-v4.6.1-f40-recovery-hotfix`.
- A Fase 40 permanece completa e preserva todas as fases anteriores.

## Build

- Versão: v4.6.1
- Build ID: VE-4.6.1-F40-HOTFIX-RECOVERY
- Data: 19/06/2026 às 10:45:00 BRT
