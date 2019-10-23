# -*- coding: utf-8 -*-

NOTAS = (100, 50, 20, 10, 5, 2)
MOEDAS = (1, 0.50, 0.25, 0.10, 0.05, 0.01)

valor = float(input())

print('NOTAS:')
for nota in NOTAS:
    print('{} nota(s) de R$ {:.2f}'.format(int(valor / nota), nota))
    valor = float('{:.2f}'.format(valor - (valor // nota) * nota))

print('MOEDAS:')
for moeda in MOEDAS:
    print('{} moeda(s) de R$ {:.2f}'.format(int(valor / moeda), moeda))
    valor = float('{:.2f}'.format(valor - (valor // moeda) * moeda))
