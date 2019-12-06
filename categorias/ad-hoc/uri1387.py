# -*- coding: utf-8 -*-

while True:
    valores = input().split()
    val_1, val_2 = int(valores[0]), int(valores[1])

    if val_1 == 0 == val_2: break

    qtd_filhos_e_filhas = val_1 + val_2
    print(qtd_filhos_e_filhas)
