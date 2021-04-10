'''
DESAFIO 013

Faça um algoritmo que leia o salário de um funcionário, e mostre
seu novo salário com 15% de aumento.
'''

salario = int(input('Digite o salário do funcionário:R$ '))

novoSalario = salario + (salario * 15 / 100)

print(f'O trabalhador que recebia R${salario}, com reajuste de 15% passará a receberR${novoSalario:.2f}')

