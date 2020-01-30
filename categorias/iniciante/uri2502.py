# -*- coding: utf-8 -*-

def decryptar(frase, len_crypt, encrypt, decrypt):
    """Para decriptar conforme as chaves de encrypt e decrypt"""
    for idx in range(len_crypt):
        frase = frase.replace(encrypt[idx], decrypt[idx])
        frase = frase.replace(encrypt[idx].lower(), decrypt[idx].lower())
    return frase


def join_decrypt(frase_original, decrypt1, decrypt2):
    """Para fazer a junção das duas frases decriptadas para gerar uma única"""
    frase_decrypt = ''
    for idx, letra in enumerate(frase_original):
        if decrypt1[idx] == letra:
            frase_decrypt += decrypt2[idx]
        else:
            frase_decrypt += decrypt1[idx]
    return frase_decrypt


def normalizar(frase_original, frase_decripitada):
    """Para normalizar a frase conforme letras UPPER e LOWER na frase original"""
    new_frase = ''
    for i, l in enumerate(frase_original):
        if l.isupper():
            new_frase += frase_decripitada[i].upper()
        else:
            new_frase += frase_decripitada[i].lower()
    return new_frase


while True:
    try:
        c, n = map(int, input().split())

        chave1 = input()
        chave2 = input()

        for i in range(n):
            frase = input()
            
            frase_decryptada_1 = decryptar(frase, c, chave1, chave2)
            frase_decryptada_2 = decryptar(frase, c, chave2, chave1)

            frase_decrypt = join_decrypt(frase, frase_decryptada_1, frase_decryptada_2)
            
            print(normalizar(frase, frase_decrypt))
            
        print()
    except EOFError:
        break
