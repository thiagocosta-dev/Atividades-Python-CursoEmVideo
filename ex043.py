'''
DESAFIO 043

Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com tabela abaixo.
- Abaixo de 18.5: abaixo do peso    - 30 até 40: obesidade
- Entre 18.5 e 25: peso ideal       - acima de 40: obersidade mórbida
- 25 até 30: sobrepeso
'''

altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é de {imc:.1f}. Portanto você está:',end=' ')
if imc < 18.5:
    print('Abaixo do peso.')
elif imc >18.5 and imc <= 25:
    print('Peso Ideal.')
elif imc > 25 and imc <= 30:
    print('Sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Obesidade.')
else:
    print('Obesidade Morbida.')


