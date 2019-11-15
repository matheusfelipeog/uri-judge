# -*- coding: utf-8 -*-

n = [ int(input()) ]

for i in range(10):
    n.append( n[-1] * 2 )

    if i == 0:
        print('N[{}] = {}'.format( 0, n[0] ))
    else:
        print('N[{}] = {}'.format( i, n[i] ))
