# -*- coding: utf-8 -*-

n = int(input())

info = {}

for i in range(n):
    x = int(input())

    if info.get(x, False):
        info[x] += 1
    else:
        info[x] = 1

indexes = list(info.keys())
indexes.sort()

for idx in indexes:
    print('{} aparece {} vez(es)'.format(idx, info[idx]))
