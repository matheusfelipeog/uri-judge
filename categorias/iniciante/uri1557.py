# -*- coding: utf-8 -*-


def create_matriz(dimensao):
    matriz =  []

    for l in range(dimensao):
        temp = []
        for c in range(dimensao):
            temp.append(0)
        matriz.append(temp)

    exp = 1
    for k, l in enumerate(matriz):
        for i, c in enumerate(l):
            if k == 0:
                matriz[k][i] = exp
                exp *= 2
            else:
                matriz[k][i] = matriz[k - 1][i] * 2 
        
    view_matriz(matriz)
        

def view_matriz(matriz):
    s = len(str(matriz[-1][-1]))
    # Converte os valores de cada linha da matriz para uma string formatada com espaços necessários
    for l in matriz: print(' '.join( map(lambda e: '{}'.format(e).rjust(s), l)) )


while True:
    n = int(input())
    if n == 0: break

    create_matriz(n)
    print()
