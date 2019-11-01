# -*- coding: utf-8 -*-

valor_n = int(input())

i = 1
while True:
    if i % valor_n == 2:
        print(i)

    i += 1
    if i > 10000:
        break
