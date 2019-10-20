# -*- coding: utf-8 -*-

a, b, c = map(float, input().split())  # map aplica a funcão float() em todos os itens da lista

area_tri_retangulo = a * c / 2
area_circulo = 3.14159 * c**2
area_trapezio = ((a + b) * c) / 2
area_quadrado = b**2
area_retangulo = a * b

print('TRIANGULO: {:.3f}'.format(area_tri_retangulo))
print('CIRCULO: {:.3f}'.format(area_circulo))
print('TRAPEZIO: {:.3f}'.format(area_trapezio))
print('QUADRADO: {:.3f}'.format(area_quadrado))
print('RETANGULO: {:.3f}'.format(area_retangulo))
