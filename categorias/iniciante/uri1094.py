# -*- coding: utf-8 -*-

n = int(input())

rato, sapo, coelho, total_cobaias = 0, 0, 0, 0
for i in range(0, n):
    qtd, tipo_cobaia = input().split()
    qtd = int(qtd)

    total_cobaias += qtd
    if tipo_cobaia == 'R':
        rato += qtd
    elif tipo_cobaia == 'S':
        sapo += qtd
    elif tipo_cobaia == 'C':
        coelho += qtd

    if i == n:
        break

print('Total: {} cobaias'.format(total_cobaias))
print('Total de coelhos: {}'.format(coelho))
print('Total de ratos: {}'.format(rato))
print('Total de sapos: {}'.format(sapo))

per_coelho = (coelho * 100) / total_cobaias
per_rato = (rato * 100) / total_cobaias
per_sapo = (sapo * 100) / total_cobaias

print('Percentual de coelhos: {:.2f} %'.format(per_coelho))
print('Percentual de ratos: {:.2f} %'.format(per_rato))
print('Percentual de sapos: {:.2f} %'.format(per_sapo))
