# -*- coding: utf-8 -*-

x = int(input())

while True:
    z = int(input())

    if z > x:
        break

cont = 0
i = x
while True:
    cont += 1

    if x > z:
        break

    x += i + 1
    i += 1

print(cont)
