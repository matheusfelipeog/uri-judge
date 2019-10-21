# -*- coding: utf-8 -*-

tempo_gasto = int(input())
velocidade_media = float(input())

#                    (     distância percorrida     ) / 12km/l
litros_necessarios = (tempo_gasto * velocidade_media) / 12

print('{:.3f}'.format(litros_necessarios))
