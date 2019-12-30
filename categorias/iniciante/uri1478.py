# -*- coding: utf-8 -*-


def create_matriz(dimensao):
    matriz = [[ '{:>3}'.format(i) for i in range(1, dimensao + 1) ]] * dimensao

    end_1 = 1
    end_2 = 2
    for i, l in enumerate(matriz):
        if i == 0: continue

        # Realiza o fatiamento de uma parte, a inverte e soma com o fatiamento de outra parte da linha
        # Exemplos: lista = [1,2,3,4,5]
        #   lista[1:2][::-1] + lista[:-1] -> tem como retorno uma lista: [2, 1, 2, 3, 4]
        matriz[i] = l[1:end_2][::-1] + l[:-end_1]
        end_1 += 1
        end_2 += 1

    view_matriz(matriz)
        

def view_matriz(matriz):
    for l in matriz: print(' '.join(l))
    

while True:
    n = int(input())
    if n == 0: break

    create_matriz(n)
    print()
