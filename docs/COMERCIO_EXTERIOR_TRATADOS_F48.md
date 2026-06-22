# Fase 48 — Comércio Exterior, Tratados Econômicos e Rotas Internacionais

Build: `VE-4.14.0-F48-COMERCIO-EXTERIOR-TRATADOS-ROTAS-INTERNACIONAIS`  
Versão: `v4.14.0`  
Data: `22/06/2026 às 22:18:00 BRT`

## Objetivo
Transformar o Vale Empires em uma simulação econômica mais profunda, onde o reino não depende apenas da economia interna, mas também de mercados estrangeiros, tratados, tarifas, importações, exportações, embargos e confiança internacional.

## Sistemas adicionados
- exportações e importações com dependência externa;
- rede de tratados econômicos;
- mercados estrangeiros com nível, XP, acesso, confiança, volume e risco;
- tarifas e eficiência alfandegária;
- contrabando e combate a perdas fiscais;
- embargo estratégico e risco de retaliação;
- credibilidade da moeda;
- autonomia estratégica;
- alcance marítimo comercial;
- interesses sociais ligados ao comércio externo.

## Integração preservada
A Fase 48 preserva o tema musical oficial da Fase 47 e todos os sistemas anteriores. O novo sistema conversa com economia interna, logística imperial, justiça, educação, províncias e recursos do jogador.

## Save
Novo campo persistido no save principal:

```json
{
  "schemaVersion": 27,
  "externalCommerce": {}
}
```

## Anti-quebra
O sistema é carregado como módulo isolado `js/external-commerce.js`, usa `window.ValeExternalCommerce`, possui armazenamento local próprio `valeEmpires.externalCommerce`, e também entra no save principal por `externalCommerce`.
