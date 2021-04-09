'''
DESAFIO 046

Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifícios,
indo de 10 até 0, com uma pausa de 1 segundo
'''

from time import sleep

for c in range(10, -1, -1):
    
    print(c)
    sleep(1)
print('BOOOOOMMM!!!!')
