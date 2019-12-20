# -*- coding: utf-8 -*-

n, k = map(int, input().split())
alunos = sorted([input() for i in range(n)])
print(alunos[k - 1])
