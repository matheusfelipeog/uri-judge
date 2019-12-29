# -*- coding: utf-8 -*-

def moviments(x1, y1, x2, y2):
    r = 2
    if x1 == x2 and y1 == y2:
        r = 0
    elif (x1 == x2 or y1 == y2) or abs(x1 - x2) == abs(y1 - y2):
        r = 1
    return r

while True:
    x1, y1, x2, y2 = map(int, input().split())

    # Caso todos sejam valores 0, será retornado False e o not irá inverter para True
    if not all([x1, x2, y1, y2]): break

    print('{}'.format(moviments(x1, y1, x2, y2)))
