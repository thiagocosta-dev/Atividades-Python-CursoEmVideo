'''
DESAFIO 015

Escreva um programa que pergunte a quantidade de KM percorridos
por um carro alugador e quantidade de dias pelos quais
ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 po dia
e R$0,15 por KM rodado.
'''

km = float(input('Quantos KM o carro rodou? KM  '))
dias = int(input('Quantos dias o carro foi alugado? '))

diaria = 60 * dias

kmRodado = 0.15 * km

precoFinal = diaria + kmRodado

print(f'O carro foi alugado por {dias} dias.\nRodando {km}KM.\nPortanto, o total a pagar será de R${precoFinal:.2f}')
