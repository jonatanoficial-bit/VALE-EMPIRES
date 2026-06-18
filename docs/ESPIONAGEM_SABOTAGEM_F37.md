# Fase 37 — Espionagem Avançada, Sabotagem e Contraespionagem

## Objetivo
Expandir a camada política do Vale Empires com uma rede de agentes secretos, missões discretas, sabotagem logística, contraespionagem e risco de descoberta.

## Sistemas adicionados

- Painel **Espionagem Secreta** na HUD.
- Quatro agentes únicos com nível e experiência.
- Seis missões secretas com custos, dificuldade e chance de sucesso.
- Métricas de rede: agentes, sigilo, infiltração, contraespionagem, suspeita e exposição.
- Eventos periódicos de inteligência.
- Exportação de relatório secreto em JSON.
- Integração com `ValeEmpiresAPI`, recursos reais e autosave.
- Integração parcial com `ValeCourtIntrigue` por registro de cartas interceptadas.

## Agentes

1. Falcão Cinzento — batedor de rotas.
2. Corvo de Ferro — sabotador logístico.
3. Escriba Velado — interceptador de cartas.
4. Mão do Porto — informante marítimo.

## Missões

- Reconhecer rotas comerciais.
- Sabotar caravana rival.
- Infiltrar porto inimigo.
- Interceptar cartas da corte.
- Operação de contraespionagem.
- Desviar suprimentos militares.

## Save

O save principal passa para `schemaVersion: 17` e inclui o campo `secretOperations`.

## Observação de design

As missões são tratadas como simulação estratégica e política, sem violência gráfica.
