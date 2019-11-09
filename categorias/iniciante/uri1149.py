# -*- coding: utf-8 -*-

v = input().split()

a = int(v.pop(0))

for i in map(int, v):
    if i > 0:
        n = i

soma = 0
for i in range(n):
    soma += a + i

print(soma)
