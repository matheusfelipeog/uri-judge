# -*- coding: utf-8 -*-

C  = int(input())
T = input()

m = []
soma = 0

for linha in range(12):
    val_linha = []
    for coluna in range(12):
        val = float(input())
        val_linha.append(val)

        if C == coluna:
            soma += val

    m.append(val_linha)

if T == 'S':
    print('{:.1f}'.format(soma))
elif T == 'M':
    print('{:.1f}'.format(soma / 12))
