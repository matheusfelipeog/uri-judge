# -*- coding: utf-8 -*-

nota = int(input())

if 86 <= nota <= 100:
    print('A')
elif 61 <= nota < 86:
    print('B') 
elif 36 <= nota < 61:
    print('C')
elif 1 <= nota < 36:
    print('D')
elif nota == 0:
    print('E')
