# -*- coding: utf-8 -*-

def soma_alg(arg):
    """Realiza a soma dos algarismos recursivamente."""
    soma = 0
    for i in arg:
        soma += int(i)

    soma = str(soma)

    if len(soma) > 1:
        soma = soma_alg(soma)
    
    return soma


def maior(v1, v2):
    """Verifica qual o maior e retorna o valor correspondente."""
    resul = 0
    if v1 > v2:
        resul = 1
    elif v1 < v2:
        resul = 2
    
    return resul


while True:
    v1, v2 = input().split(' ')

    if v1 == v2 == '0':
        break
    
    # Chamada da função recursiva para os dois valores.
    # O returno será verificado pela função "maior" 
    resultado = maior(soma_alg(v1), soma_alg(v2))
    print(resultado)
