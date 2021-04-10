'''
DESAFIO 031

Desenvola um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem,cobrando R$0,50 por Km para viagens até 200Km
e R$0,45 para viagens mais longas.

'''

viagem = float(input('Qual distãncia da sua viagem? '))

if viagem <= 200:
    preco = viagem * 0.50

else:
    preco = viagem * 0.45

print(f'Sua viagem foi de Km {viagem}. Portanto, pagará R${preco}')