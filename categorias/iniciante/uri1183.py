# -*- coding: utf-8 -*-

O = input()

m = []
soma = 0

for linha in range(12):
    valores_linha = []
    for coluna in range(12):

        valores_linha.append(float(input()))

        if coluna > linha:
            soma += valores_linha[-1]

    m.append(valores_linha)

if O == 'S':
    print('{:.1f}'.format(soma))
elif O == 'M':
    print('{:.1f}'.format(soma / 66))
