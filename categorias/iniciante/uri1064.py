# -*- coding: utf-8 -*-

i, cont_positivo, acumula_positivo = 0, 0, 0
while True:
    valor = float(input())

    if valor > 0:
        cont_positivo += 1
        acumula_positivo += valor

    i += 1
    if i == 6:
        break

print('{} valores positivos'.format(cont_positivo))
print('{:.1f}'.format(acumula_positivo / cont_positivo))
