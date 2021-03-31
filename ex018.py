'''
DESAFIO 018

Faça um programa que leia um angulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo.
''' 
from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de: {seno:.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de: {coss:.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de: {tang:.2f}')
