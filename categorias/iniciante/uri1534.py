# -*- coding: utf-8 -*-

while True:
    try:
        N = int(input())

        # Aqui é populada uma matriz N por N com compressão de lista, contido em cada posição o valor string '3'.
        # É feito uma cópia de cada linha ( que é uma lista de valores '3' ) dessa matriz para não manter a referência de ID na memória
        matriz_123 = [linha.copy() for linha in [['3'] * N] * N]

        coluna_do_valor_2 = N - 1

        for num_linha in range(N):
            matriz_123[num_linha][num_linha] = '1'
            matriz_123[num_linha][coluna_do_valor_2] = '2'
            coluna_do_valor_2 -= 1

            print(''.join(matriz_123[num_linha]))

    except EOFError:
        break
