# -*- coding: utf-8 -*-

while True:
    try:
        l = input()

        v = map(int, input().split())

        veloz = max(v)

        if veloz < 10: print(1)
        elif  10 <= veloz < 20: print(2)
        else: print(3)

    except EOFError:
        break
