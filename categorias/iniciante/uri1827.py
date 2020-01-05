# -*- coding: utf-8 -*-

def create_matriz(dimensao):

    m = [['0' for i in range(dimensao)] for i in range(dimensao)]
    
    diag_princ = 0
    diag_secun = dimensao - 1
    interno = dimensao // 3

    for i, l in enumerate(m):
        for k, c in enumerate(l):
     
            if (k >= interno and k <= len(m) - interno - 1):
                if i > interno - 1 and i <= len(m) - interno - 1:
                    m[i][k] = '1'
                else:
                    m[i][diag_princ] = '2'
                    m[i][diag_secun] = '3'

        diag_princ += 1
        diag_secun -= 1

    if dimensao % 2 != 0:
        centro = dimensao // 2
        m[centro][centro] = '4'

    view_matriz(m)

def view_matriz(matriz):
    for l in matriz:
        print( ''.join(l) )

while True:
    try:
        create_matriz(int(input()))
        print()
    except EOFError:
        break
