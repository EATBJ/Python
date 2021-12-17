import numpy as np
from random import randint

zeros = matrix_int(10,10)

zr = np.zeros(shape=(10,10))
ent = 's'
while ent == 's':
      #print('\n')
      print('Sortear novo número?')
      ent = input('(s) = Sim / (n) = Não: ')
      print('\n')
      if ent == 's':
           l_soted = randint(0,9)
           c_sorted = randint(0,9)
           sorted = int(zeros[l_soted][c_sorted])
           #zeros[l_soted][c_sorted] = 0
           if sorted == 0:
             while sorted == 0:
                   l_soted = randint(0,9)
                   c_sorted = randint(0,9)
                   sorted = int(zeros[l_soted][c_sorted])
             zeros[l_soted][c_sorted] = 0
             zr[l_soted][c_sorted] = sorted
             print('Número sorteado é: ', sorted,'\n')
           else: 
             zeros[l_soted][c_sorted] = 0
             zr[l_soted][c_sorted] = sorted
             print('Número sorteado é: ', sorted,'\n')
           
      else:
          print('Fim do sorteio\n')
      print('Os numeros sorteados até o momento são:')
      print(zr)
      print('+++++++++++++++++++++++++++++++++++++++++++')
      print('\n')
