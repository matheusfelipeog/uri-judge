# -*- coding: utf-8 -*-

a, b, c = map(int, input().split())  # map aplica a funcão int() em todos os itens da lista

maiorAB = (a + b + abs(a - b)) // 2
maior = (c + maiorAB + abs(c - maiorAB)) // 2

print('{} eh o maior'.format(maior))
