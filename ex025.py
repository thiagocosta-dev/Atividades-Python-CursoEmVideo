'''
Desafio 025

Crie um programa que leia o nome de uma  pessoal e diga se ela tem
'SILVA' no nome
'''

nome = str(input('Digite seu nome completo: ')).upper().strip().split()

print('Seu nome tem Silva? {}'.format('SILVA' in nome))
