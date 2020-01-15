# -*- coding: utf-8 -*-

a = ['Roberto', '', '5786', '', 'UNIFEI']
print('-' * 39, end='')
for i in a:
    print('\n|{:^8}'.format('') + '{:<29}|'.format(i), end='')
print('\n' + '-' * 39)
