# -*- coding: utf-8 -*-

n = int(input())

calc = 0
for i in range(n):
    calc += 6.0
    calc = 1/calc

print('{:.10f}'.format(calc + 3))
