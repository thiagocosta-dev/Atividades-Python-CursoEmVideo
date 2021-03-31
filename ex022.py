'''
DESAFIO 022

Crie um programa que leia o nome completo de uma pessoa e 
mostre:

> Nome com todas as letras maiusculas e minusculas.
> Quantas letras tem(sem espaços).
> Quantas letras temp 1° nome.
'''

nome = str(input('Digite seu nome: ')).strip()

print(f'Nome maiúsculo: {nome}'.upper())
print(f'Nome minúsculo: {nome}'.lower())
print(f'Quantas letras tem: {len(nome.strip()) - nome.count(" ")}')
print(f'O primeiro nome tem:{nome.find(" ")} ')

