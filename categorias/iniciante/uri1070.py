# -*- coding: utf-8 -*-

valor_x = int(input())

i = 0
while True:
    if valor_x % 2 != 0:
        print(valor_x)
        valor_x += 2
    else:
        valor_x += 1
        continue

    i += 1
    if i == 6:
        break
