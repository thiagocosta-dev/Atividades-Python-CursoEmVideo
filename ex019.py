'''
DESAFIO 019

Faça um programa que leia o  nome de 4 alunos
e sorteie um deles.
'''
from random import choice

a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

lista = [a1, a2, a3, a4]

print(f'O aluno sorteado foi: {choice(lista)}')

