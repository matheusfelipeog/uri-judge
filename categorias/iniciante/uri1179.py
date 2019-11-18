# -*- coding: utf-8 -*-

def lista_vetores(tipo, vetor):
    for idx, valor in enumerate(vetor):
        print('{}[{}] = {}'.format(tipo, idx, valor))


vet_par, vet_impar = [], []
for c in range(15):
    val = int(input())

    if val % 2 == 0:
        vet_par.append(val)
    else:
        vet_impar.append(val)
    
    if len(vet_par) == 5:
        lista_vetores('par', vet_par)
        vet_par = []
    elif len(vet_impar) == 5:
        lista_vetores('impar', vet_impar)
        vet_impar = []

lista_vetores('impar', vet_impar)
lista_vetores('par', vet_par)
