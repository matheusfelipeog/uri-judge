# -*- coding: utf-8 -*-

L = int(input())
T = input()

m = []

for linha in range(12):
    val_linha = []
    for coluna in range(12):

        val_linha.append(float(input()))

    m.append(val_linha)

if T == 'S':
    soma = sum(m[L])
    print('{:.1f}'.format(soma))
elif T == 'M':
    media = sum(m[L]) / 12
    print('{:.1f}'.format(media))
