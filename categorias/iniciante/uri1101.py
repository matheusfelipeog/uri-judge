# -*- coding: utf-8 -*-

while True:
    m, n = map(int, input().split())

    if m <= 0 or n <= 0:
        break

    if m < n:
        soma = 0
        for c in range(m, n + 1):
            print(c, end=' ')
            soma += c
        print('Sum={}'.format(soma))
    elif m > n:
        soma = 0
        for c in range(n, m + 1):
            print(c, end=' ')
            soma += c
        print('Sum={}'.format(soma))
    else:
        print('{} Sum={}'.format(m, m))
