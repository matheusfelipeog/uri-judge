# -*- coding: utf-8 -*-

n = int(input())

i, cont_in, cont_out = 0, 0, 0
while True:
    valor = int(input())

    if 10 <= valor <= 20:
        cont_in += 1
    else:
        cont_out += 1

    i += 1
    if i == n:
        break

print('{} in'.format(cont_in))
print('{} out'.format(cont_out))
