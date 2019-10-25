# -*- coding: utf-8 -*-

def imprime_valores(lista, sort):
    lista.sort() if sort else lista

    for valor in lista:
        print(valor)


lista_valores = list(map(int, input().split()))

imprime_valores(lista_valores.copy(), True)
print()
imprime_valores(lista_valores, False)
