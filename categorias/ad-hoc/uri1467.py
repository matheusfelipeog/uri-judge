# -*- coding: utf-8 -*-

p = {0: 'A', 1: 'B', 2: 'C'}

while True:
    try:
        rodada = input().split()

        if rodada.count('0') == 1:
            idx = rodada.index('0')
        elif rodada.count('1') == 1:
            idx = rodada.index('1')
        else:
            print('*')
            continue

        print(p[idx])
        
    except EOFError:
        break
