# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    amigo = input().split()

    if amigo[0] != 'Thor':
        print('N')
    else:
        print('Y')
