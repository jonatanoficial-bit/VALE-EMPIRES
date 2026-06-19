# Roteiro de Teste Manual — Fase 41

1. Subir a build no GitHub/Vercel.
2. Limpar cache do site ou usar Ctrl+F5.
3. Confirmar no canto da tela a versão `v4.7.0 Fase 41`.
4. Entrar em uma partida nova ou continuar um save.
5. Tocar no botão de economia da HUD.
6. Conferir abertura do painel `Economia Interna e Abastecimento do Reino`.
7. Alterar política fiscal.
8. Investir em um setor produtivo.
9. Aplicar uma medida econômica com recursos suficientes.
10. Salvar a partida.
11. Recarregar o navegador.
12. Continuar o save e confirmar que `internalEconomy` foi restaurado.
13. Testar modo recuperação e botão voltar.
14. Instalar como PWA e repetir o acesso ao painel.

## Resultado esperado

- Nenhum erro `classList` no console.
- Painel abre e fecha normalmente.
- Save/load preserva economia interna.
- Recursos e estatísticas econômicas mudam com ações e ciclos.
