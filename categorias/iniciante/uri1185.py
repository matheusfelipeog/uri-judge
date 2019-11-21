# -*- coding: utf-8 -*-

O = input()

m = []
soma = 0
diagonal_excluida = 11

for linha in range(12):
    valores_linha = []
    for coluna in range(12):

        valores_linha.append(float(input()))

        if coluna < diagonal_excluida:
            soma += valores_linha[-1]

    diagonal_excluida -= 1
    m.append(valores_linha)

if O == 'S':
    print('{:.1f}'.format(soma))
elif O == 'M':
    print('{:.1f}'.format(soma / 66))
