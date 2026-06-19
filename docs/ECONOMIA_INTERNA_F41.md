# Fase 41 — Economia interna, abastecimento, impostos e classes produtivas

## Objetivo

Transformar a camada social da Fase 40 em consequência econômica real dentro do reino: recursos, mercado doméstico, impostos, abastecimento, preços, corrupção, mercado paralelo, classes produtivas e risco de crise interna.

## Sistemas adicionados

### 1. Saúde econômica

A saúde econômica combina:

- prosperidade;
- abastecimento;
- confiança do mercado;
- liquidez mercantil;
- apoio das classes produtivas;
- estabilidade cultural/religião/civilização;
- identidade nacional;
- penalidades por preço alto, imposto abusivo, corrupção, mercado paralelo, desemprego e tensão social.

### 2. Política fiscal

Quatro caminhos estratégicos:

- Tributação equilibrada;
- Alívio ao povo;
- Imposto de guerra;
- Autonomia mercantil.

Cada política altera receita, confiança, tensão social e estabilidade produtiva.

### 3. Setores produtivos

Quatro setores com nível e XP:

- Campos e celeiros;
- Oficinas artesanais;
- Minas e fundições;
- Construção civil.

Investimentos aumentam eficiência e geram efeitos na economia.

### 4. Classes produtivas

Seis grupos sociais/econômicos:

- Camponeses;
- Artesãos;
- Mercadores;
- Mineiros;
- Construtores;
- Guardas urbanos.

Cada grupo possui apoio, tensão e influência.

### 5. Medidas econômicas

Sete ações com custo, chance e risco:

- Abrir celeiros reais;
- Carta das grandes feiras;
- Auditar coletores de impostos;
- Subsidiar guildas produtivas;
- Tribunal dos preços abusivos;
- Estradas rurais e armazéns;
- Reforma monetária da coroa.

### 6. Ciclos automáticos

A cada ciclo, o sistema pode:

- gerar ouro por impostos e liquidez;
- estabilizar alimento quando há bom abastecimento;
- aumentar preço por escassez;
- aumentar mercado paralelo quando há corrupção;
- criar crise econômica quando a saúde econômica cai.

## Integração técnica

- Script: `js/internal-economy.js`.
- Dataset: `data/economy/internal-economy.json`.
- Botão HUD: `btnInternalEconomyPanel`.
- LocalStorage: `valeEmpires.internalEconomy`.
- Save principal: campo `internalEconomy`.
- Save schema: `21`.
- APIs usadas: `ValeEmpiresAPI.spend`, `ValeEmpiresAPI.addStock`, `ValeEmpiresAPI.getSnapshot`, `ValeEmpiresAPI.saveQuiet`.

## Integração com fases anteriores

- Fase 40: usa estabilidade e identidade nacional.
- Fase 39: usa moral/cultura quando disponível.
- Fases 33–34: usa snapshot de províncias e recursos.
- Núcleo RTS: altera ouro/alimento e lê estoque/armazenamento.

## Anti-quebra

- Se o botão da HUD não existir, o script apenas não vincula o evento.
- Se a API principal ainda não estiver pronta, o sistema usa fallback seguro.
- Se o JSON salvo estiver corrompido, o normalizador recria estado válido.
- O overlay é criado dinamicamente para não depender de HTML fixo.
