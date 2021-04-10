'''
DESAFIO 032

Escreva um programa para aprovar um empréstimo bancário para compra de casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''

casa = float(input('Qual valor da casa? R$'))
salario = float(input('Qual salário do comprador? '))
anos = int(input('Em quantos anos será pago? '))

prestacao = casa / (anos * 12)


if prestacao > (salario * 30 / 100):
    print(f'''A casa no valor de R${casa:.2f}, com salário de R${salario:.2f}, com {anos} anos de empréstimo, ficará com a prestação no valor de R${prestacao:.2f}.
Excedendo 30% do salário, portanto, empréstimo será NEGADO.''')

else:
    print(f'''A casa no valor de R${casa:.2f}, com salário de R${salario:.2f}, com {anos} anos de empréstimo, ficará com a prestação no valor de R${prestacao:.2f}.
NÃO excedendo 30% do salário, portanto, empréstimo será ACEITO.''')
