'''
DESAFIO 011

Faça um programa que leia altura e largura de uma parede. Calcule a sua área e a quantidade de tinta necessária para pintar.
 Sabendo que que cada litro de tinta pinta uma área de 2m².
'''

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura: '))
area = altura * largura
tinta = area / 2
print(f'Sua parede tem {altura} de altura,  {largura} de largura, logo sua área é de {area}m².\nA quantidade necessária de tinta para pintá-la será de {tinta} litros.')
