# -*- coding: utf-8 -*-

n = int(input())

for c in range(n):
    s1, s2 = input().split()
    
    out = ''
    for v in zip(s1, s2):
        out += ''.join(v)

    out += s1[len(s2):]
    if len(s2) > len(s1):
        out += s2[len(s1):]
    
    print(out)
