# -*- coding: utf-8 -*-

while True:
    soma_nota = 0
    for i in range(2):

        nota = float(input())

        while not(0 <= nota <= 10):
            print('nota invalida')
            nota = float(input())

        soma_nota += nota

    print('media = {:.2f}'.format(soma_nota / 2))

    op = int(input('novo calculo (1-sim 2-nao)\n'))

    while not(op in (1,2)):
        op = int(input('novo calculo (1-sim 2-nao)\n'))

    if op == 2:
        break
