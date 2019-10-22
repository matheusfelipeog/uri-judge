# -*- coding: utf-8 -*-

t_segundos = int(input())

t_minutos = t_segundos // 60
t_segundos -= (t_minutos * 60)

t_hora = t_minutos // 60
t_minutos -= (t_hora * 60)

print('{}:{}:{}'.format(t_hora, t_minutos, t_segundos))
