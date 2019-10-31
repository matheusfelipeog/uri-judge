# -*- coding: utf-8 -*-

n = int(input())

i = 0
while True:
    valor = int(input())

    if valor % 2 == 0 and valor > 0:
        print('EVEN POSITIVE')
    elif valor % 2 == 0 and valor < 0:
        print('EVEN NEGATIVE')

    elif valor % 2 != 0 and valor > 0:
        print('ODD POSITIVE')
    elif valor % 2 != 0 and valor < 0:
        print('ODD NEGATIVE')

    else:
        print('NULL')
        
    i += 1
    if i >= n:
        break
