# -*- coding: utf-8 -*-

h_inicio, m_inicio,  h_fim, m_fim = map(int, input().split())

horas = h_fim - h_inicio
if h_inicio > h_fim:
    horas = h_fim - h_inicio + 24

minutos = m_fim - m_inicio
if m_inicio > m_fim:
    minutos += 60
    horas -= 1

if horas == minutos == 0:
    horas = 24

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
