'''
DESAFIO 010

Crie um programa que leia um valor em reais e converta para dólar.
Considere 1.00 US$ = 3,27R$

'''
valor = float(input('Digite o valor a ser convertido: '))
conversao = valor / 3.27
print(f'{valor:.2f}R$ convertidos em dólar ficam {conversao:.2f}')
