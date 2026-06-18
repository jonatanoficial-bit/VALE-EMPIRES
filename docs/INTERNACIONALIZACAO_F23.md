# Internacionalização — Fase 23

## Arquitetura
O jogo usa `js/i18n.js` com dicionários internos anti-quebra e cópias oficiais em `locales/`.

## Idiomas suportados
- `pt-BR`
- `en-US`
- `es-ES`

## Persistência
A preferência é salva em `localStorage` na chave `valeEmpires.language`.

## Segurança dos saves
Os saves continuam armazenando IDs como `england`, `feudal`, `infantry` e chaves de tecnologias. Os nomes traduzidos são apenas apresentação. Assim, a troca de idioma não altera a lógica nem corrompe campanhas.

## Conteúdo dinâmico
Um observador de DOM traduz textos criados depois da inicialização, incluindo modais, alertas, objetivos, pesquisas e mensagens da IA. Regras de padrões cobrem números, porcentagens e nomes interpolados.

## Fallback
Qualquer chave ausente mantém o texto original em português. Isso evita telas vazias e preserva a jogabilidade.
