# -*- coding: utf-8 -*-


def verifica_multiplo(multiplo):
    if not multiplo:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')


a, b = map(int, input().split())

if a > b:
    verifica_multiplo(a % b)
else:
    verifica_multiplo(b % a)
