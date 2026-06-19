# Fase 40 — Religião/Civilização, tradições profundas, facções sociais e identidade nacional

## Objetivo da fase

Transformar a camada social do Vale Empires em uma simulação mais profunda de civilização, identidade nacional e estabilidade popular. A fase expande a Fase 39 de Moral e Cultura, mas cria um sistema separado para pactos civilizacionais, tradições e facções sociais.

## Sistemas adicionados

### 1. Pacto civilizacional

O jogador escolhe um modelo abstrato de organização social:

- Coroa Sagrada do Vale;
- Comunidade Cívica;
- Lei Ancestral;
- Acordo das Tradições.

Cada pacto altera legitimidade, espiritualidade fictícia, tolerância, autonomia local, unidade, agitação e tensão faccional.

### 2. Tradições profundas

Foram adicionadas tradições com nível e XP:

- Calendário Sagrado Fictício;
- Épico Nacional;
- Costumes das Aldeias;
- Pedras de Juramento;
- Escolas de Escribas.

Elas impactam memória comum, identidade nacional, unidade, autonomia, tolerância e estabilidade popular.

### 3. Facções sociais

Foram adicionadas seis facções sociais:

- Ordem espiritual;
- Nobreza regional;
- Guildas urbanas;
- Aldeias e camponeses;
- Exército e veteranos;
- Sábios e cronistas.

Cada facção possui apoio, tensão e influência. A mediação reduz risco de ruptura social.

### 4. Identidade nacional

A identidade nacional combina memória comum, unidade, legitimidade, tradições e tensão social. A métrica é usada para medir a força simbólica do reino.

### 5. Estabilidade popular avançada

A estabilidade popular combina legitimidade, espiritualidade fictícia, tolerância, autonomia, unidade, identidade, memória comum, coesão provincial, moral cultural e apoio das facções.

## Integração com fases anteriores

- Usa `window.ValeCulturalMorale.score()` quando disponível.
- Usa `window.ValeEmpiresAPI.getSnapshot().provinceCohesion` quando disponível.
- Salva em `localStorage` com a chave `valeEmpires.religionCivilization`.
- Integra no save principal no campo `religionCivilization`.
- Restaura pelo método `window.ValeReligionCivilization.restore()`.

## Observação de design

O sistema é fictício e abstrato. A proposta é simular dinâmicas sociais, civis e simbólicas de um reino medieval fictício, sem representar doutrinas reais ou promover intolerância.
