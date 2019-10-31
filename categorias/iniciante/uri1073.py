# -*- coding: utf-8 -*-

n = int(input())

i = 2
while True:
    print('{}^2 = {}'.format(i, i**2))

    i += 2
    if i > n:
        break
