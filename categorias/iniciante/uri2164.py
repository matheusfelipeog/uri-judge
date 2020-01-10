# -*- coding: utf-8 -*-

def fibo(value):
    raiz = 5 ** 0.5
    return (((1 + raiz) / 2) ** value - ((1 - raiz) / 2) ** value) / raiz

value = int(input())

print('{:.1f}'.format(fibo(value)))
