# -*- coding: utf-8 -*-

distancia_percorrida = int(input())
tot_combustivel_gasto = float(input())

consumo_medio = distancia_percorrida / tot_combustivel_gasto

print('{:.3f} km/l'.format(consumo_medio))
