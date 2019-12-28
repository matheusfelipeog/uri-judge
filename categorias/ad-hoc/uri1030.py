# -*- coding: utf-8 -*-

def flav(n, k):
    r = 0
    for i in range(2, n + 1):
        r = (r + k) % i
    return r + 1  # Somar + 1, pois caso contrário sempre estará uma unidade a menos do valor esperado

nc = int(input())

for i in range(nc):

    n, k = map(int, input().split())
    print('Case {}: {}'.format(i + 1 , flav(n, k) ))
