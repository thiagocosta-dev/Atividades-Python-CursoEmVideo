'''
DESAFIO 008

Crie um programa que converta uma valor em metros recebido pelo teclado, em centímetros e milímetros.
'''

metros = float(input('Digite um valor em metros: '))
cent = metros * 100
mili = metros * 1000
print(f'{metros} convertidos para centímetros da {cent} e em milímetros é {mili}')
