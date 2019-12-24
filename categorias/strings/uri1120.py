# -*- coding: utf-8 -*-

while True:
    d, n = input().split()

    if d == n == '0': break

    n = n.replace(d, '')

    # Caso todos os valores em 'n' for iguais a 'd'
    # será armazenado o valor 0 em 'n', caso contrário, o valor já
    # contido em 'n' será convertido para inteiro
    n = int(n) if n != '' else 0

    print(n)
