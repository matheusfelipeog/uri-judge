# -*- coding: utf-8 -*-

i, cont_posi, cont_nega, cont_par, cont_impar = 0, 0, 0, 0, 0
while True:
    valor = int(input())

    if valor > 0: cont_posi += 1
    if valor < 0: cont_nega += 1

    if valor % 2 == 0: cont_par += 1
    if valor % 2 != 0: cont_impar += 1

    i += 1
    if i == 5: break

print('{} valor(es) par(es)'.format(cont_par))
print('{} valor(es) impar(es)'.format(cont_impar))
print('{} valor(es) positivo(s)'.format(cont_posi))
print('{} valor(es) negativo(s)'.format(cont_nega))
