# -*- coding: utf-8 -*-

n, m = map(int, input().split())

partidas = []
for i in range(n):
    partida = map(int, input().split())

    # Acrescenta lista dentro da lista de partidas
    partidas.append( list(partida) )  

pontuadores = 0
for gols in partidas:

    # True se valores for maior que 0 na lista de gols, senão False
    if all(gols):  
        pontuadores += 1

print(pontuadores)
