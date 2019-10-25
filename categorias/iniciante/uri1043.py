# -*- coding: utf-8 -*-

a, b, c = map(float, input().split())

if abs(b - c) < a < b + c or abs(a - c) < b < a + c or abs(b - a) < c < b + a:
    print('Perimetro = {:.1f}'.format(a + b + c))
else:
    print('Area = {:.1f}'.format( ((a + b) * c) / 2))
