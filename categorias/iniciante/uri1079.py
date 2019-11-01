# -*- coding: utf-8 -*-

n = int(input())

i = 0
while True:
    nota1, nota2, nota3 = map(float, input().split())

    print('{:.1f}'.format((nota1 * 2 + nota2 * 3 + nota3 * 5) / 10))

    i += 1
    if i >= n:
        break
