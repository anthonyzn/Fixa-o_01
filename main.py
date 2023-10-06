import numpy as np

#Criar um array bidimensional
matriz = np.array([[9, 11, 4],
                  [3, 3, 3],
                  [1, 7, 6]])

#Obter dados estatísticos diferentes
#média
media_coluna = np.mean(matriz, axis=0)
print(f'A média das colunas é:\n{media_coluna}')

#Obter dados estatísticos diferentes
#minima
min_linhas = np.min(matriz, axis=1)
print(f'O menor valor das linhas são:\n{min_linhas}')

#Obter dados estatísticos diferentes
#soma sem axis
soma_matriz = np.sum(matriz)
print(f'A soma de cada elemento da matriz é: \n{soma_matriz}')

#Obter a transposta da matriz...
transposta = matriz.T
print(transposta)

#E realizar uma operação com ela
print(transposta[0,1])
print(matriz[0,2])
operação = (transposta [0, 1] + matriz [0, 2])
print(f'A soma desses dois índices é: {operação}')


#Produto escalar entre duas matrizes ou de um array com uma matriz
mat1 = np.array([[3, 5, 9], [2, 3, 6]])
mat2 = np.array([[3, 5, 9], [2, 3, 6], [7, 1, 8]])
print(f'Matriz 1:\n {mat1}\n')
print(f'Matriz 2:\n{mat2}\n')

escalar = np.dot(mat1, mat2)
print(f'O produto escalar é:\n {escalar}')

#Criar um filtro para a sua matriz

filtro = matriz %2 == 0
m_pares = matriz[filtro]
print(f'A matriz original é essa:\n {matriz}')

print(f'\nA nova matriz só com números pares: \n{m_pares}')

#Realizar alguma operação aritmética (número com matriz, array com matriz, etc.);
num = 42

adicao = matriz[0, :] + num
print(f'Qual o resultado dos elementos da primeira linha + 42?\n{adicao}')

adicao1 = matriz[2, 1] + num
print(f'Qual o resultado do 2º elem da 3ª linha + 42?\n{adicao1}')
