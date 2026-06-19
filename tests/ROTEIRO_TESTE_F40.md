# Roteiro de Teste Manual — Fase 40

1. Abrir o jogo no navegador.
2. Confirmar build visível `VE-4.6.1-F40-HOTFIX-RECOVERY`.
3. Entrar em campanha ou continuar save existente.
4. Tocar no botão de HUD **Religião, Civilização e Identidade Nacional**.
5. Confirmar abertura do painel premium.
6. Alterar o pacto civilizacional.
7. Fortalecer uma tradição profunda.
8. Mediar uma facção social.
9. Executar uma decisão de estabilidade popular.
10. Salvar a partida.
11. Recarregar o jogo e continuar o save.
12. Confirmar que `religionCivilization` foi restaurado.
13. Exportar o dossiê JSON pelo painel.
14. Testar rolagem do painel no mobile.
15. Testar PWA instalada em tela cheia.

## Critérios de aprovação

- Painel abre sem erro.
- Botões respondem ao toque.
- Métricas mudam após ações.
- Save/load preserva a Fase 40.
- Não há perda dos sistemas das Fases 35–39.


## Hotfix v4.6.1

Validar que o menu inicial carrega sem acionar modo de recuperação por `classList` nulo e que o cache PWA recebeu novo nome.
