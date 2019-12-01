# -*- coding: utf-8 -*-

N = int(input())

i = 0
while True:    
    palavra = list(input())

    for idx in range(len(palavra)):
        if palavra[idx].isalpha():
            palavra[idx] = chr(ord(palavra[idx]) + 3)
    
    palavra = palavra[::-1]

    for idx in range( len(palavra) // 2, len(palavra) ):
        palavra[idx] = chr(ord(palavra[idx]) - 1)

    print(''.join(palavra))

    i += 1
    if i >= N: break
