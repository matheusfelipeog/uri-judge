# -*- coding: utf-8 -*-

i = 1
while True:
    for j in range(7, 4, -1):
        print('I={} J={}'.format(i, j))

    i += 2
    if i > 9:
        break
