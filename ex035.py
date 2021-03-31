'''
DESAFIO 037

Desenvolva um programa que leia ocomprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo
'''

r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r2 + r1:
    print('Os seguimentos acima PODEM formar triângulo.')
else:
    print('Os seguimentos acima NÃO PODEM formar triangulo.')
