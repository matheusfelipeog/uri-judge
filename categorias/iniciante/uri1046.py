# -*- coding: utf-8 -*-

inicio, fim = map(int, input().split())

horas = fim - inicio
if inicio > fim:
    horas += 24

if horas == 0:
    horas = 24

print('O JOGO DUROU {} HORA(S)'.format(horas))
