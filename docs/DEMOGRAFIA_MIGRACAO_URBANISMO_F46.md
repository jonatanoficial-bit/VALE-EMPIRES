# Fase 46 — Demografia, Migração, Habitação e Urbanismo

Build: `VE-4.12.0-F46-DEMOGRAFIA-MIGRACAO-URBANISMO`  
Versão: `v4.12.0`  
Save schema: `26`

## Objetivo

Adicionar uma camada populacional profunda ao Vale Empires: crescimento do povo, migração, moradia, bairros, emprego urbano, integração cultural, famílias, superlotação, sem-teto e risco de distúrbios sociais.

## Sistemas adicionados

- Índice populacional, crescimento, migração, controle migratório e força de trabalho.
- Habitação, urbanismo, emprego, integração cultural, natalidade e estabilidade familiar.
- Superlotação, falta de moradia e risco de distúrbio.
- Distritos urbanos com nível, XP, cobertura e bônus progressivos.
- Grupos populacionais com apoio, tensão e influência.
- Doutrinas sociais e medidas demográficas com custo, chance, sucesso e falha.
- Dossiê JSON exportável.

## Integrações preservadas

A Fase 46 consulta opcionalmente saúde pública, economia interna, logística imperial, justiça, educação e religião/civilização. Todas as chamadas são protegidas por `optional chaining`, sem dependência obrigatória.

## Persistência

O save principal recebeu a chave `demographyUrbanism`. O schema subiu para `26`. O módulo também mantém uma cópia segura em `localStorage` para recuperação isolada.

## Anti-quebra

- Overlay criado dinamicamente.
- Botão ausente é ignorado.
- Integrações externas opcionais.
- Exportação JSON sem bibliotecas externas.
- Sem alteração destrutiva nos sistemas anteriores.
