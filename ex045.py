'''
DESAFIO 45

Crie um programa que faça o computador jogar JOKENPÔ com você.
'''

from random import randint
from time import sleep
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

usuario = int(input('Qual sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)
print('=' * 25)
if usuario == 0:
    if usuario == 0 and computador == 0:
        print('EMPATE! Você escolheu PEDRA e o computador escolheu PEDRA.')
    elif usuario == 0 and computador == 1:
        print('PERDEU! Você escolheu PEDRA e o computador escolheu PAPEL.')
    else:
        print('GANHOU! Você escolheu PEDRA e o computador escolheu TESOURA.')
elif usuario == 1:
    if usuario == 1 and computador == 1:
        print('EMPATE! VOcÊ escolheu PAPEL e o computador escolheu PAPEL.')
    elif usuario == 1 and computador == 0:
        print('GANHOU! Você escolheu PAPEL e o computador escolheu PEDRA.')
    else:
        print('PERDEU! Você escolheu PAPEL e o computador escolheu TESOURA.')
elif usuario == 2:
    if usuario == 2 and computador == 2:
        print('EMPATE! Você escolheu TESOURA e o computador escolheu TESOURA.')
    elif usuario == 2 and computador == 0:
        print('PERDEU! Você escolheu TESOURA e o computador escolheu PEDRA.')
    else:
        print('GANHOU! Você escolheu TESOURA e o computador escolheu PAPEL.')
