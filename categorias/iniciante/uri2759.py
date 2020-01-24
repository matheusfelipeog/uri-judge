# -*- coding: utf-8 -*-

v = [input() for i in range(3)]

for i in range(3):
    print('A = {}, B = {}, C = {}'.format(*v))
    v[0], v[1], v[2] = v[1], v[2], v[0]
