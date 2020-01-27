# -*- coding: utf-8 -*-

n = input()

obj = map(int, n.split('.')[::-1])

print('{}.{}'.format(*obj))
