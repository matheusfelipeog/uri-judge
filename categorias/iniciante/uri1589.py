# -*- coding: utf-8 -*-

T = int(input())

for i in range(T):
    R1, R2 = map(int, input().split())

    print(((R1 + R2) * 2) // 2)
