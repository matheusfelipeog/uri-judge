# -*- coding: utf-8 -*-

n = int(input())

i = 0
while True:

    x, y = map(int, input().split())

    if y == 0:
        print('divisao impossivel')
    else:
        print('{:.1f}'.format(x / y))

    i += 1
    if i >= n:
        break
