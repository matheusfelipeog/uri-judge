# -*- coding: utf-8 -*-

x = [int(input()) for i in range(10)]

for c in range(len(x)):

    if x[c] < 1:
        x[c] = 1

    print('X[{}] = {}'.format(c, x[c]))
