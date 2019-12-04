# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    string = input()
    key = int(input())
    
    print(''.join(( chr(ord(l) - key) if ord(l) - key >= 65 else chr(ord(l) - key + 26) for l in string )))
