# -*- coding: utf-8 -*-

acms = []

for i in range(2):
    acm = map(int, input().split())
    acms.append( list(acm) )

compativel = True

# O zip junta todos os itens de mesmo índice dentro de tuplas 
for hard_acm in zip(*acms):  # Use * para retirar todos elementos de dentro da lista
    
    # hard_acm contém uma tupla de itens de mesmo índice.
    # Por exemplo: acms = [ [0, 1, 1], [1, 0, 0] ]
    # hard_acm itera sobre o seguinte Zip Object
    # convertido para lista: [ (0, 1), (1, 0), (1, 0) ]
    # Agora só comparar os valores da tupla no índice 0 e 1
    if hard_acm[0] == hard_acm[1]:
        compativel = False
        break

if compativel: print('Y')
else: print('N')
