# -*- coding: utf-8 -*-

idades, c = [], 0
while True:
    idade = int(input())

    if idade < 0:
        break

    idades.append(idade)
    c += 1

media_idade = sum(idades) / c
print('{:.2f}'.format(media_idade))
