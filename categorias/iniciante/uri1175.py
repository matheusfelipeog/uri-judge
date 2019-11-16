# -*- coding: utf-8 -*-

n = [ int(input()) for i in range(20) ]

n.reverse()

for c in range( len(n) ):
    print('N[{}] = {}'.format( c, n[c] ))
