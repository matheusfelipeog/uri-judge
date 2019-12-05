# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    caract = input()
    val_1, string, val_2, resul = int(caract[0]), caract[1], int(caract[-1]), 0

    if val_1 == val_2:
        resul = val_1 * val_2
    elif string.isupper():
        resul = val_2 - val_1
    elif string.islower():
        resul = val_1 + val_2

    print(resul)
