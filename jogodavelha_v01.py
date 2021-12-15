from mymod import verify_winer, display_board, player_input, print_board

A = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

print('Escolha seu Jogador:')
print('Jogador 1 = " X "')
print('Jogador 2 = " O "\n')
print('Imprimindo tabuleiro ...\n')
print_board(A)

res = 1

while res == 1:

    #print('Digite o n° do jogador (1 ou 2):')
    plr = input('Digite o n° do jogador (1 ou 2):')
    print('\n')

    l,c = player_input(plr)

    A = display_board(l,c,plr,A)
    
    res, plr = verify_winer(A,plr)

