# -*- coding: utf-8 -*-

a, b = (float(i) for i in input().split())

porcentagem = (b - a) * 100 / a

print('{:.2f}%'.format(porcentagem))
