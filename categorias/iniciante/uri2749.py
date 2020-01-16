# -*- coding: utf-8 -*-

print('-' * 39, end='')
for i in range(5):
    if i == 0:
        print('\n|{:<37}|'.format('x = 35'), end='')
    elif i == 2:
        print('\n|{:^37}|'.format('x = 35'), end='')
    elif i == 4:
        print('\n|{:>37}|'.format('x = 35'), end='')
    else:
        print('\n|{:<37}|'.format(''), end='')
print('\n' + '-' * 39)
