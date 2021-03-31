'''
DESAFIO 016

Crie um programa que leia um número Real e mostre na tela sua porção inteira.
'''
from math import trunc
num = float(input('Digite um número: '))

print(f'O número {num} tem a porção inteira {trunc(num)}')

