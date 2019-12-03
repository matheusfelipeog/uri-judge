# -*- coding: utf-8 -*-

n = int(input())

led_necessarios = {
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6,
    '0': 6
}

i = 0
while True:
    valor = input()
    qtd_led = 0

    for num in valor:
        qtd_led += led_necessarios[num]

    print('{} leds'.format(qtd_led))

    i += 1
    if i >= n:
        break
