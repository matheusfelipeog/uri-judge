# -*- coding: utf-8 -*-

x, y = int(input()), int(input())

soma_nao_mult = 0
if x < y:
    for i in range(x, y + 1):
        if i % 13 != 0:
            soma_nao_mult += i
elif x > y:
    for i in range(y, x + 1):
        if i % 13 != 0:
            soma_nao_mult += i

print(soma_nao_mult)