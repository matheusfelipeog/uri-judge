# -*- coding: utf-8 -*-

qtd_caso_teste = int(input())

i = 0
while True:
    tempo = 0

    pa, pb, g1, g2 = map(float, input().split())
    pa, pb = int(pa), int(pb)

    while True:

        pa += int(( g1 / 100 * pa))
        pb += int(( g2 / 100 * pb))
        tempo += 1
        
        if tempo > 100:
            print('Mais de 1 seculo.')
            break

        if pa > pb:
            print('{} anos.'.format(tempo))
            break
        
    i += 1
    if i >= qtd_caso_teste:
        break
