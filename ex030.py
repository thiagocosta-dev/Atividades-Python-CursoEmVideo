'''
DESAFIO 030

Crie um programa que leia um número inteiro e mostre se é par ouy ímpar.
'''

num = int(input('Digite um número: '))

resultado = num % 2

if resultado == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é impar')
