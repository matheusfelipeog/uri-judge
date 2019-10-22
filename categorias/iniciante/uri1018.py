# -*- coding: utf-8 -*-

NOTAS = (
    100, 50, 20,
    10, 5, 2, 1
)

valor = int(input())

print(valor)
for nota in NOTAS:
    # Quantidade de notas de Nº valor, e o valor formatado com , (vírgula)
    print('{} nota(s) de R$ {:.2f}'.format(valor // nota, nota).replace('.', ','))
    valor -= (valor // nota) * nota  # Subtraí as notas já mostradas
