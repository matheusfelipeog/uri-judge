# -*- coding: utf-8 -*-

t = int(input())

valores = list(range(t))

vetor = []
i = 0

for c in range(1000):
    vetor.append(valores[i])

    i += 1
    if i > len(valores) - 1:
        i = 0

for idx, val in enumerate(vetor):
    print('N[{}] = {}'.format(idx, val))
