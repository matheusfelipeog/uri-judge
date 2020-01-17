# -*- coding: utf-8 -*-

def head(*arg):
    print('|  {}  |  {}  |  {}  |'.format(*arg))

def line(qtd):
    print('-' * qtd)


def body(end):
    for i in range(end + 1):
        print('|     {:2}    |   {:2}    |       {}       |'.format(i, i if i < 8 else i + 2, hex(i)[2:].upper()))

line(39)
head('decimal', 'octal', 'Hexadecimal')
line(39)
body(15)
line(39)
