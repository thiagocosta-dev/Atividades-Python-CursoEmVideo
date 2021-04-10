'''
DESAFIO 006

Crie um algoritmo que leia um número e mostre seu dobro,triplo e raiza quadrada.
'''
from math import sqrt
num = int(input('Digite um número: '))
dob = num * 2
tri = num * 3
raiz = sqrt(num)
print(f'O dobro de {num} é {dob},\no triplo {tri},\na raiza quadrada é {raiz}.')
