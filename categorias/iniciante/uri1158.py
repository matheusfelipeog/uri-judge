# -*- coding: utf-8 -*-

n = int(input())

i = 0
while True:
    s = 0

    x, y = map(int, input().split())

    # Para descobrir quantas iterações deve fazer, basta mutiplicar
    #  o valor de ' y ' por 2 e somar com o valor de ' x '
    for c in range(x, x + y * 2):
        if c % 2 != 0:
            s += c
    print(s)

    i += 1
    if i >= n:
        break
