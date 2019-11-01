# -*- coding: utf-8 -*-

n = int(input())

i = 1
while True:
    print('{} x {} = {}'.format(i, n, i * n))

    i += 1
    if i > 10:
        break
