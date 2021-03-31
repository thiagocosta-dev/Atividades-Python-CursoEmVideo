'''
DESAFIO 029

Escreva um porgrama que leia a velocidade de um carro.
Se ultrapassar 80Km/h mostre a mensagem dizendo que foi multado
A multo vai custar R$7.00 por cada Km acima do limite.

'''

carro = float(input('Digite a velocidade do carro: Km/h '))

if carro <= 80:
    print('Dirija com segurança!')
else:
    print('Excedeu limite de velocidade!')
    multa = (carro - 80) * 7
    print(f'Você pagará R${multa:.2f} de multa')
