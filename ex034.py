'''
DESAFIO 034
Escreva um programa que pergunte o salário do funcionário e calcule valor
do aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.

'''

salario = float(input('Qual salário do funcionário? R$'))

if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
    print(f'O salário do funcionário que era R${salario:.2f} com aumento de 15%, passa a ser R${aumento:.2f}')

else:
    aumento = salario + (salario * 10 / 100)
    print(f'O salário do funcionário que era R${salario:.2f} com aumento de 10%, passa a ser R${aumento:.2f}')
