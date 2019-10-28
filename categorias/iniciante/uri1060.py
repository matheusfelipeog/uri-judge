# -*- coding: utf-8 -*-

i = 0
positivos = 0
while True:
    valor = float(input())

    if valor > 0: positivos += 1

    i += 1
    if i == 6: break

print('{} valores positivos'.format(positivos))
