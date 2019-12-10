# -*- coding: utf-8 -*-

def raiz_2(n):
    if n == 0:
        return 2
    else:
        calc = 2 + 1 / raiz_2(n - 1)
        return calc

print('{:.10f}'.format(raiz_2(int(input())) - 1))
