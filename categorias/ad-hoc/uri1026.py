# -*- coding: utf-8 -*-    

def format_bin(number):
    """Formata um número para sua representação binária de 32 bits"""
    return  '{:0>32b}'.format(number)

while True:
    try:
        
        values = map(int, input().split())
        bin_a, bin_b = map(format_bin, values)
        
        new_bin = ''  # Para construção do novo binário
        for v1, v2 in zip(bin_a, bin_b):
            if v1 != v2: new_bin += '1'
            else: new_bin += '0'
        
        print(int(new_bin, 2))  # Convertendo o novo binário para decimal

    except EOFError:
        break
