# -*- coding: utf-8 -*-


grenais, vit_inter, vit_gremio, empate = 0, 0, 0, 0
while True:
    gol_inter, gol_gremio = map(int, input().split())
    grenais += 1

    if gol_inter > gol_gremio:
        vit_inter += 1
    elif gol_inter < gol_gremio:
        vit_gremio += 1
    else:
        empate += 1

    op = int(input('Novo grenal (1-sim 2-nao)\n'))

    if op != 1:
        break

print('''{} grenais
Inter:{}
Gremio:{}
Empates:{}'''.format(grenais, vit_inter, vit_gremio, empate))

if vit_inter > vit_gremio:
    print('Inter venceu mais')
elif vit_inter < vit_gremio:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
