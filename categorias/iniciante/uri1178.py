# -*- coding: utf-8 -*-

x = float(input())

vet = [x]

for c in range(99):
    vet.append(vet[-1] / 2)

for idx, val in enumerate(vet):
    print('N[{}] = {:.4f}'.format(idx, val))
