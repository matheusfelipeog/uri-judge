# -*- coding: utf-8 -*-

i = cont_par = 0
while True:
    valor = int(input())

    if valor % 2 == 0: cont_par += 1

    i += 1
    if i == 5: break

print('{} valores pares'.format(cont_par))
