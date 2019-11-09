# -*- coding: utf-8 -*-

x, y = map(int, input().split())

for i in range(1, y + 1):
    # Caso o valor de i não seja divisível pelo valor de x
    if i % x != 0:
        print(i, end=' ')
    else:
        print(i)
