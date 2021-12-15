def display_board(linha,coluna,plr,A):

  if plr == '1':
    A[linha][coluna] = 'X'
  else:
    A[linha][coluna] = 'O'

  print('      0','   1','   2 \n','  ','+---','+---','+---+\n',
      '0-','|',A[0][0],' |',A[0][1],' |',A[0][2],'|','\n','  ',
        '+---','+---','+---+\n',
      '1-','|',A[1][0],' |',A[1][1],' |',A[1][2],'|','\n','  ',
        '+---','+---','+---+\n',
      '2-','|',A[2][0],' |',A[2][1],' |',A[2][2],'|','\n','  ',
        '+---','+---','+---+\n')
  B = [[A[0][0],A[0][1],A[0][2]],[A[1][0],A[1][1],A[1][2]],[A[2][0],A[2][1],A[2][2]]]

  return B


def verify_winer(A,plr):
  
     if   (A[0][0] == A[1][1] and A[0][0] == A[2][2]) and (A[0][0] != ' '):
        print('player', plr, 'winer')
        res = 0
     elif (A[0][2] == A[1][1] and A[0][2] == A[2][0]) and (A[0][2] != ' '):
        print('player', plr, 'winer')
        res = 0
     elif (A[0][0] == A[0][1] and A[0][0] == A[0][2]) and (A[0][0] != ' '):
        print('player', plr, 'winer')
        res = 0
     elif (A[1][0] == A[1][1] and A[1][0] == A[1][2]) and (A[1][0] != ' '):
        print('player', plr, 'winer')
        res = 0
     elif (A[2][0] == A[2][1] and A[2][0] == A[2][2]) and (A[2][0] != ' '):
        print('player', plr, 'winer')
        res = 0
     elif (A[0][0] == A[1][0] and A[0][0] == A[2][0]) and (A[0][0] != ' '):
        print('player', plr, 'winer')
        res = 0
     elif (A[0][1] == A[1][1] and A[0][1] == A[2][1]) and (A[0][1] != ' '):
        print('player', plr, 'winer')
        res = 0
     elif (A[0][2] == A[1][2] and A[0][2] == A[2][2]) and (A[0][2] != ' '):
        print('player', plr, 'winer')
        res = 0
     else:
        print('continue...\n')
        res = 1
        if plr == '1':
          print('Próximo será o Jogador 2\n\n')
        else:
          print('Próximo será o Jogador 1\n\n')
     return res, plr


def player_input(plr):

    print('Jogador', plr,'digite as coordenadas:\n')
    linepl = input('linha:')
    linepl = int(linepl)
    colupl = input('coluna:')
    colupl = int(colupl)
    print('As coordenadas do jogador', plr,'são: ', '(',linepl,',',colupl,')\n')
    return linepl, colupl
    
def print_board(A):

    print('      0','   1','   2 \n','  ','+---','+---','+---+\n',
          '0-','|',A[0][0],' |',A[0][1],' |',A[0][2],'|','\n','  ',
            '+---','+---','+---+\n',
          '1-','|',A[1][0],' |',A[1][1],' |',A[1][2],'|','\n','  ',
            '+---','+---','+---+\n',
          '2-','|',A[2][0],' |',A[2][1],' |',A[2][2],'|','\n','  ',
            '+---','+---','+---+\n')
    pass
