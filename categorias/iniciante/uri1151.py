# -*- coding: utf-8 -*-

n = int(input())

seq_fibo = [0, 1]

for i in range(2, n):

    seq_fibo.append(seq_fibo[i - 2 ] + seq_fibo[i - 1])

print(' '.join(map(str, seq_fibo)))
