# -*- coding: utf-8 -*-

maior, idx_maior = 0, 0
for i in range(1, 101):
    valor = int(input())

    if valor > maior:
        maior = valor
        idx_maior = i

print(maior)
print(idx_maior)
