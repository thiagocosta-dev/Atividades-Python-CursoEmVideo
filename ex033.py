'''
DESAFIO 033

Faça um programa que leia três números e mostre qual é o maior e qual é menor
'''

n1 = int(input('1° Número: '))
n2 = int(input('2° Número: '))
n3 = int(input('3° Número: '))


if n1 > n2 and n1 > n3:
    maior = n1

elif n2 > n1 and n2 > n3:
    maior = n2

else:
    maior = n3


if n1 < n2 and n1 < n3:
    menor = n1

elif n2 < n1 and n2 < n3:
    menor = n2

else:
    menor = n3

print(f'O maior é: {maior}')
print(f'O menor é: {menor}')

