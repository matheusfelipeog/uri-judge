# -*- coding: utf-8 -*-

p1 = list(map(float, input().split()))
p2 = list(map(float, input().split()))

# dis = raiz( (X2  -   X1 )²     + (Y2    -   Y1 )² )
distancia = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5  # 0.5 = raiz

print('{:.4f}'.format(distancia))
