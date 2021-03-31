'''
DESAFIO 017

Faça um programa que leia o comprimento do cateto oposto e do adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''

from math import hypot

catetoOp = float(input('Cateto oposto: '))

catetoAj = float(input('Cateto adjacente: '))

hi = hypot(catetoOp, catetoAj)
print(f'Cateto oposto mede: {catetoOp}\nCateto adjascente: {catetoAj}\nPortante a hipotenusa é: {hi:.2f}')

