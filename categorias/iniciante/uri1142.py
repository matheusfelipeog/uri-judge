# -*- coding: utf-8 -*-

n = int(input())

i = 0
inicio = 1
limite = 5
while True:
    for num in range(inicio, limite):
        if num % 4 != 0:
            print(num, end=' ')
        else:
            print('PUM')
            
    inicio = limite
    limite += 4

    i += 1
    if i >= n:
        break
