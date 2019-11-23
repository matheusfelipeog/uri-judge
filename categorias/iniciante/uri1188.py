# -*- coding: utf-8 -*-

O = input()

matriz = []
somatorio, coluna_del = 0, 11

for linha in range(12):
    valores_da_linha = []
    for coluna in range(12):

        valores_da_linha.append(float(input()))

        if linha > 6 and coluna < linha and coluna > coluna_del:
            somatorio += valores_da_linha[-1]

    coluna_del -= 1
    matriz.append(valores_da_linha)

if O == 'S':
    print('{:.1f}'.format(somatorio))
elif O == 'M':
    print('{:.1f}'.format(somatorio / 30))
