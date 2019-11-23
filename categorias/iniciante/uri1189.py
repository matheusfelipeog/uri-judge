# -*- coding: utf-8 -*-

O = input()

matriz, somatorio, coluna_del = [], 0, 11

for linha in range(12):
    valores_linha = []

    for coluna in range(12):
        valores_linha.append(float(input()))

        if coluna < 5 and coluna < linha and coluna < coluna_del:
            somatorio += valores_linha[-1]

    matriz.append(valores_linha)
    coluna_del -= 1        

if O == 'S':
    print('{:.1f}'.format(somatorio))
elif O == 'M':
    print('{:.1f}'.format(somatorio / 30))
