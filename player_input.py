def player_input(plr):
    print('Jogador', plr,'digite as coordenadas:\n')
    linepl = input('linha:')
    linepl = int(linepl) # converte de str p/ int
    colupl = input('coluna:')
    colupl = int(colupl) # converte de str p/ int
    print('As coordenadas do jogador', plr,'são: ', '(',linepl,',',colupl,')\n')
    return linepl, colupl
    
