# -*- coding: utf-8 -*-

tabela = [
    [0, 400.00, 0.15],
    [400.01, 800.00, 0.12],
    [800.01, 1200.00, 0.10],
    [1200.01, 2000.00, 0.07]
]

salario = float(input())

reajuste_ganho = 0
porcentagem = 0

for linha in tabela:
    salario_minimo, salario_maximo, porcentagem = linha

    if salario_minimo <= salario <= salario_maximo:
        reajuste_ganho = salario * porcentagem
        salario += reajuste_ganho
        break
else:
    porcentagem = 0.04
    reajuste_ganho = salario * porcentagem
    salario += reajuste_ganho

print('Novo salario: {:.2f}'.format(salario))
print('Reajuste ganho: {:.2f}'.format(reajuste_ganho))
print('Em percentual: {:.0f} %'.format(porcentagem * 100))
