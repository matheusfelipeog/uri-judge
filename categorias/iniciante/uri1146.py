# -*- coding: utf-8 -*-

while True:
    x = int(input())

    if x == 0:
        break
    
    l = []
    for i in range(1, x + 1):
        l.append(str(i))
    
    print((' '.join(l)))
