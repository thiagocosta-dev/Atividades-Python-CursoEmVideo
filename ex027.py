'''
DESAFIO 027

Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e último nome.
'''

n = str(input('Digite seu nome completo: ')).strip()

nome = n.split()

print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[-1]}')

