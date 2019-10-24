# -*- coding: utf-8 -*-

LANCHES = [
    None,
    [1, 'Cachorro Quente', 4.00],
    [2, 'X-Salada', 4.50],
    [3, 'X-Bacon', 5.00],
    [4, 'Torrada simples', 2.00],
    [5, 'Refrigerante', 1.50]
]

codigo, quantidade = map(int, input().split())

print('Total: R$ {:.2f}'.format(quantidade * LANCHES[codigo][-1]))
