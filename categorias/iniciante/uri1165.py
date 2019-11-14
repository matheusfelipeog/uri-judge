# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    x = int(input())

    qtd_div = 0
    for c in range(1, x + 1):
        if x % c == 0:
            qtd_div += 1
            
        if qtd_div > 2:
            break
    
    if qtd_div == 2:
        print('{} eh primo'.format(x))
    else:
        print('{} nao eh primo'.format(x))
