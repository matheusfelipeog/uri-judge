# -*- coding: utf-8 -*-

p1, c1, p2, c2 = map(int, input().split())

lado_d = p1 * c1
lado_e = p2 * c2

if lado_d < lado_e:
    print(1)
elif lado_d > lado_e:
    print(-1)
else:
    print(0)
