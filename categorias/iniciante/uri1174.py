# -*- coding: utf-8 -*-

a = [ float(input()) for i in range(100) ]

for c in range( len(a) ):
    
    if a[c] <= 10:
        print('A[{}] = {}'.format( c, a[c] ))
