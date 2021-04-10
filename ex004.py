'''
DESAFIO 004

Faça um programa que leia algo pelo teclado, e mostre em seguida seu tipo primitivo e todas informações sobre ela.

'''

a = input('Digite algo: ')
print('O tipo primitivo desse valor é, ', type(a))
print('Só tem espaços: ', a.isspace())
print('É numérico: ', a.isnumeric())
   
