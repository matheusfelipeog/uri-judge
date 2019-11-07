# -*- coding: utf-8 -*-

alcool, gasolina, diesel = 0, 0, 0
while True:
    op = int(input())

    while op not in (1, 2, 3, 4):
        op = int(input())

    if op == 4:
        break

    if op == 1:
        alcool += 1
    elif op == 2:
        gasolina += 1
    elif op == 3:
        diesel += 1

print('''MUITO OBRIGADO
Alcool: {}
Gasolina: {}
Diesel: {}'''.format(alcool, gasolina, diesel))
