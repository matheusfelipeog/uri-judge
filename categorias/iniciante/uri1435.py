# -*- coding: utf-8 -*-


def create_matriz(d):
    m = []

    for l in range(d):
        temp = []
        for c in range(d):
            temp.append(0)
        m.append(temp)

    meio = round(d / 2 + 0.3)

    v = 1
    t_or_l = 0  # Value of Top or Left
    b_or_r = d - 1  # Value of Bottom or Right

    while True:
        if v > meio: break

        idx = t_or_l
        # Set values in Top and Bottom
        for i in range(idx, b_or_r + 1):
            m[t_or_l][i] = v
            m[b_or_r][i] = v

        idx = t_or_l + 1
        # Set values in Left and Right
        for i in range(idx, b_or_r):
            m[i][t_or_l] = v
            m[i][b_or_r] = v
            
        v += 1
        t_or_l += 1
        b_or_r -= 1

    view_matriz(m)


def view_matriz(m):
    for l in m:
        print(' '.join( map(lambda e: '{:>3}'.format(e), l) ))


while True:
    n = int(input())
    if n == 0: break

    create_matriz(n)
    print()
