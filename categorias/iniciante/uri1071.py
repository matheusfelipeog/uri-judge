# -*- coding: utf-8 -*-

x = int(input())
y = int(input())

soma_impar = 0
if x > y:
    for valor in range(x-1, y, -1):
        if valor % 2 != 0:
            soma_impar += valor
    print(soma_impar)
    
elif x < y:
    for valor in range(y, x, -1):
        if valor % 2 != 0:
            soma_impar += valor
    print(soma_impar)
    
else:
    print(0)
