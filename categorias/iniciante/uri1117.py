# -*- coding: utf-8 -*-

soma_nota = 0
for i in range(2):

    nota = float(input())

    while not(0 <= nota <= 10):
        print('nota invalida')
        nota = float(input())

    soma_nota += nota

print('media = {:.2f}'.format(soma_nota / 2))
