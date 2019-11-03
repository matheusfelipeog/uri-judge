# -*- coding: utf-8 -*-

i = 1
j = 7
while True:
    for c in range(j, j - 3, -1):
        print('I={} J={}'.format(i, c))

    i += 2
    j += 2
    if i > 9:
        break
