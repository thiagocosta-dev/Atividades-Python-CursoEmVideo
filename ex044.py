'''
DESAFIO 044

Elabore um programa que calcule o valor a ser pago por um produto,considerando o ser preço normal
e condição do pagamento:
- à vista dinheiro/cheque: 10% desconto
- à vista cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% juros
'''

print('========== ALINE MELL MAKE ================')
preco = float(input('Preço das compras: R$ '))

print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cartão
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
print('========== ALINE MELL MAKE ================')
if opcao == 1:
    valor = preco - (preco * 10 / 100)
    print(f'Sua compra de R${preco:.2f} vai custar R${valor:.2f}. Com o desconto de 10%. ')
elif opcao == 2:
    valor = preco - (preco * 5 / 100)
    print(f'A compra de R${preco:.2f}, ficará R${valor:.2f}. Com desconto de 5%.')
elif opcao == 3:
    print(f'Sua com ficará R${preco:.2f}.')
elif opcao == 4:
    divisao_cartao = int(input('Em quantas vezes? '))
    valor = preco + (preco * 20 / 100)
    print(f'A compra de R${preco:.2f} com aumento de 20% ficará R${valor:.2f}')
else:
    print('Valor inválido. Tente novamente.')

