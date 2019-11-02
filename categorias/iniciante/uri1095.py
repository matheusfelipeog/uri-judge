# -*- coding: utf-8 -*-

i = 1
j = 60
while True:
    print('I={} J={}'.format(i, j))
    i += 3
    j -= 5

    if j < 0:
        break
