# Fase 44 — Educação, Conhecimento e Ciência do Reino

Build: **VE-4.10.0-F44-EDUCATION-KNOWLEDGE**  
Versão: **v4.10.0**  
Schema de save: **24**

## Objetivo

Esta fase adiciona uma camada profunda de educação, ciência, tradição escrita, formação técnica, universidade, burocracia e mobilidade social ao Vale Empires. O reino passa a evoluir não apenas por exército e economia, mas pela capacidade de formar pessoas, preservar memória, inovar e administrar melhor o território.

## Sistemas adicionados

- Painel HUD **Educação e Conhecimento** (`btnEducationKnowledgePanel`).
- Módulo `js/education-knowledge.js` com overlay dinâmico anti-quebra.
- Dados estratégicos em `data/society/education-knowledge.json`.
- Persistência no save principal pelo campo `educationKnowledge`.
- Integração com `ValePublicHealth`, `ValeInternalEconomy`, `ValeReligionCivilization` e `ValeImperialLogistics`.
- Exportação de dossiê JSON.

## Métricas principais

- Alfabetização.
- Erudição.
- Arquivos.
- Universidade.
- Mestres.
- Técnica.
- Educação cívica.
- Burocracia.
- Inovação.
- Mobilidade social.
- Resistência ao novo.
- Fuga de talentos.
- Pressão das elites.

## Instituições

1. Escolas de aldeia.
2. Salões dos escribas.
3. Biblioteca real.
4. Colégio universitário.
5. Oficinas-escola.
6. Academia militar.

## Doutrinas educacionais

- Escolas de templo e tradição.
- Alfabetização cívica.
- Universidade régia.
- Aprendizado das guildas.
- Exames do serviço real.

## Medidas jogáveis

- Copiar livros e mapas.
- Contratar mestres estrangeiros.
- Fundar escolas paroquiais.
- Patrocinar debates da universidade.
- Treinar oficiais e escribas.
- Padronizar ofícios e medidas.

## Anti-quebra

O módulo cria o overlay dinamicamente, ignora botão ausente com segurança, usa optional chaining para integrações e mantém normalização dos dados antes de salvar/restaurar.
