# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    x = int(input())

    soma_div = 0
    for c in range(1, x):
        if x % c == 0:
            soma_div += c
    
    if soma_div == x:
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))

    if i >= n: break
