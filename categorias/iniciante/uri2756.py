# -*- coding: utf-8 -*-

array = [
    '{:>8}'.format('A'),
    '{0:>7}{0:>2}'.format('B'),
    '{0:>6}{0:>4}'.format('C'),
    '{0:>5}{0:>6}'.format('D'),
    '{0:>4}{0:>8}'.format('E')
]

def print_losango(array):
    for i in array:
        print(i)

print_losango(array)
print_losango(array[-2::-1])  # Fatia a string 'E' do array
