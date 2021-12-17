def matrix_int(line,colum): 
  #Cria uma matriz de numeros inteiros com:
  #N° de linhas igual a linha
  #E N° de colunas igual a colunas

  # Necessita de importação do numpy como np
  
  zeros = np.zeros(shape=(line,colum))
  nn = 0
  for l in range(line):
      for c in range(colum):
          zeros[l][c] = int(nn)
          nn +=1
  return zeros
