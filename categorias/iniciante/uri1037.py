# -*- coding: utf-8 -*-

valor = float(input())

INTERVALOS = (
    range(0, 26), range(25, 51),
    range(50, 76), range(75, 101)
)

for intervalo in INTERVALOS:
    if intervalo[0] <= valor <= intervalo[-1] and intervalo == INTERVALOS[0]:
        print('Intervalo [{},{}]'.format(intervalo[0], intervalo[-1]))
        break
    elif intervalo[0] + 0.01 <= valor <= intervalo[-1]:
        print('Intervalo ({},{}]'.format(intervalo[0], intervalo[-1]))
        break
else:
    print('Fora de intervalo')
