# -*- coding: utf-8 -*-

nome_vendedor = input()
salario_fixo = float(input())
tot_venda_mes = float(input())

salario_total = salario_fixo + (tot_venda_mes * 0.15)

print('TOTAL = R$ {:.2f}'.format(salario_total))
