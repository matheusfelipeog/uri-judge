# -*- coding: utf-8 -*-

salario = float(input())

if 0.0 <= salario <= 2000.00:
    print('Isento')
elif 2000.01 <= salario <= 3000.00:
    imposto = ((salario - 2000) * 0.08)
    print('R$ {:.2f}'.format(imposto))
    
elif 3000.01 <= salario <= 4500.00:
    imposto = (1000 * 0.08) + ((salario - 3000) * 0.18)
    print('R$ {:.2f}'.format(imposto))

elif salario > 4500.00:
    imposto = (1000 * 0.08) + (1500 * 0.18) + ((salario - 4500) * 0.28)
    print('R$ {:.2f}'.format(imposto))
