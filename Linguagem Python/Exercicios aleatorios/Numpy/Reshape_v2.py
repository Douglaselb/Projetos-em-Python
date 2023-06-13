# Continuação do método reshape()

import numpy as np

matriz = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
'''
Neste caso o terceiro valor permite que o numpy determine o tamanho da terceira dimensão
com base nos valores anteriores e o total da matriz original
'''
modificada = matriz.reshape(2, 2, -1)
print('Matriz original\n', modificada.base)
print('\nTerceira modficada:\n', modificada)

'''
    O valor -1 faz a matriz n-D ser uma matriz 1-D
    Outra maneira que apresenta o mesmo resultado é o método flatten() e o ravel()
'''
modificada = modificada.reshape(-1)
print('\nRetorno da reshape(-1)\n', modificada)
