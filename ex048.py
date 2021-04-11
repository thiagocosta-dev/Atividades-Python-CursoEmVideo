'''
DESAFIO 048

Faça um programa que calcule a soma entre todos números impares que são multiplos de três e que
se encontram no intervalo de 1 até 500.
'''
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
        soma = soma + c
        
print(f'A soma de todos os {contador} valores solicitados é: {soma}.')

