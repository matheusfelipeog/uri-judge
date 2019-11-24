# -*- coding: utf-8 -*-

O = input()

matriz, somatorio, coluna_del = [], 0, [0, 11]

for linha in range(12):
    valores_linha = []

    for coluna in range(12):
        valores_linha.append(float(input()))
        
        if coluna > 6 and coluna > linha and coluna > coluna_del[0] and coluna > coluna_del[1]:
            somatorio += valores_linha[-1]

    matriz.append(valores_linha)
    coluna_del[0] += 1      
    coluna_del[1] -= 1      

if O == 'S':
    print('{:.1f}'.format(somatorio))
elif O == 'M':
    print('{:.1f}'.format(somatorio / 30))
