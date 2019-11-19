# -*- coding: utf-8 -*-

n = int(input())

vetor = list(map(int, input().split()))
menor = (0, vetor[0])

for idx in range(n):
    if vetor[idx] < menor[1]:
        menor = (idx, vetor[idx])

print('Menor valor: {}'.format(menor[1]))
print('Posicao: {}'.format(menor[0]))
