# -*- coding: utf-8 -*-

num = input()

if num[0] != '-':
    r =  '+' + '{:.4E}'.format( float(num) )
else:
    r = '{:.4E}'.format( float(num) )

print( r )
