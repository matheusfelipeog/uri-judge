# -*- coding: utf-8 -*-

v = [input() for i in range(3)]

for i in range(4):
    if i == 3:
        print('{:.10}{:.10}{:.10}'.format(*v))
        continue
    print('{}{}{}'.format(*v))

    v[0], v[1], v[2] = v[1], v[2], v[0]
    