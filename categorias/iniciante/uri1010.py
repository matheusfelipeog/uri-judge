# -*- coding: utf-8 -*-

compra_1 = input().split()
compra_2 = input().split()

val_a_pagar = (int(compra_1[1]) * float(compra_1[2]) + int(compra_2[1]) * float(compra_2[2]))

print('VALOR A PAGAR: R$ {:.2f}'.format(val_a_pagar))
