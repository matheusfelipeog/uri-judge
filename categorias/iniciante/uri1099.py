# -*- coding: utf-8 -*-


def calc_impar(ini, fim):
    tot_impar = 0
    for c in range(ini + 1, fim):
        if c % 2 != 0:
            tot_impar += c
    print(tot_impar)


n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    if x < y:
        calc_impar(x, y)
            
    elif x > y:
        calc_impar(y, x)
    else:
        print(0)
