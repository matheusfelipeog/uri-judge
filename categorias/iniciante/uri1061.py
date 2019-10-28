# -*- coding: utf-8 -*-

dia_inicio = int(input()[3:])
h_inicio, m_inicio, s_inicio = map(int, input().split(' : '))
dia_fim = int(input()[3:])
h_fim, m_fim, s_fim = map(int, input().split(' : '))

segundos = s_fim - s_inicio
minutos = m_fim - m_inicio
horas = h_fim - h_inicio
dias = dia_fim - dia_inicio

if segundos < 0:
    segundos += 60
    minutos -= 1

if minutos < 0:
    minutos += 60
    horas -= 1

if horas < 0:
    horas += 24
    dias -= 1

print('{} dia(s)'.format(dias))
print('{} hora(s)'.format(horas))
print('{} minuto(s)'.format(minutos))
print('{} segundo(s)'.format(segundos))
