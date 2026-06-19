# Fase 45 — Justiça, Leis e Ordem Civil do Reino

Build: `VE-4.11.0-F45-JUSTICE-LAW-CIVIL-ORDER`  
Versão: `v4.11.0`  
Save schema: `25`

## Objetivo

Transformar a autoridade do jogador em uma estrutura jurídica profunda, com tribunais, leis, crimes, costumes, prisões, apelações, corrupção e legitimidade. O sistema amplia o simulador civilizacional e prepara o caminho para conflitos internos mais complexos nas próximas fases.

## Sistemas adicionados

- Estado de direito, tribunais, decretos reais e costumes locais.
- Guarda civil, prisões, ordem civil e taxa de crime.
- Corrupção judicial, legitimidade, apelações, educação jurídica, equilíbrio de força e risco de tirania.
- Instituições jurídicas com nível, XP e cobertura.
- Facções civis com apoio, tensão e influência.
- Doutrinas legais com impactos permanentes.
- Medidas de justiça com custo, chance, sucesso, falha e eventos.
- Dossiê JSON exportável.

## Integrações preservadas

A Fase 45 consulta opcionalmente os sistemas de educação, economia interna, religião/civilização, saúde pública e logística imperial. Todas as chamadas usam `optional chaining`, sem dependência obrigatória.

## Persistência

O save principal recebeu a chave `justiceLaw`. O schema subiu para `25`. O módulo também mantém uma cópia segura em `localStorage` para recuperação isolada.

## Anti-quebra

- Overlay criado dinamicamente.
- Botão ausente é ignorado.
- Integrações externas opcionais.
- Exportação JSON sem bibliotecas externas.
- Sem alteração destrutiva nos sistemas das fases anteriores.
