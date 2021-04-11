'''
DESAFIO 050

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.

'''

acumulador = 0
pares = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        pares = pares + 1
        acumulador = acumulador + num
print(f'Você digitou {pares} números pares. E a soma entre eles é: {acumulador}')
