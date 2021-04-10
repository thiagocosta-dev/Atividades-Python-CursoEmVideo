'''
DESAFIO 038

Escreva um programa que leia dois números interios e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Os valores são iguais.
'''

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

if valor1 > valor2:
    print(f'O primeiro valor é maior.')
elif valor2 > valor1:
    print(f'O segundo valor é maior.')
else:
    print(f'Os valores são iguais.')
