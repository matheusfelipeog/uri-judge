# -*- coding: utf-8 -*-

i = 0
j = 1
while True:

    for c in range(3):
        c += j
        if i in (0, 1, 2) or i > 1.8:
            print('I={:.0f} J={:.0f}'.format(i, c))
        else:
            print('I={:.1f} J={:.1f}'.format(i, c))

    j += 0.2
    i += 0.2
    if i > 2:
        break
