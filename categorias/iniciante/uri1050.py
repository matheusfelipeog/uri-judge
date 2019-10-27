# -*- coding: utf-8 -*-

table = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'
}

ddd_informado = int(input())

for ddd, estado in table.items():
    if ddd_informado == ddd:
        print(estado)
        break
else:
    print('DDD nao cadastrado')
