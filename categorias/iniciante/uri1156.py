# -*- coding: utf-8 -*-

s = 1
div = 2
for i in range(3, 40, 2):
    s += i / div
    div *= 2

print('{:.2f}'.format(s))
