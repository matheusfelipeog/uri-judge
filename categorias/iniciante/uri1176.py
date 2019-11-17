# -*- coding: utf-8 -*-

t = int(input())

for i in range(t):
    
    n = int(input())

    c, fibo = 0, [0, 1]
    while True:

        fibo.append( fibo[-2] + fibo[-1] )
        
        c += 1
        if c >= n:
            print('Fib({}) = {}'.format( n, fibo[n] ))
            break
