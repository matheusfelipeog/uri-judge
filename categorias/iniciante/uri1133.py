# -*- coding: utf-8 -*-

x, y = int(input()), int(input())

if x < y:
    for i in range(x + 1, y):
        if i % 5 == 2 or i % 5 == 3:
            print(i)
elif x > y:
    for i in range(y + 1, x):
        if i % 5 == 2 or i % 5 == 3:
            print(i)
