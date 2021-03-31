'''
DESAFIO 012

Faça um algoritmo que leia um preço de um produto e mostre seu novo preço com desconto de 5%.

'''

preco = float(input('Digite o preço do produto: R$ '))
desconto = (preco * 5) / 100
precoFinal = preco - desconto

print(f'Seu produto que custava {preco}R$,com desconto de 5% passará a custar {precoFinal:.2f}R$')
