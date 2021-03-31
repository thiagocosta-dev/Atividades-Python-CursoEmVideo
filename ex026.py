'''
DESAFIO 026

Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes a letra 'A' apareceu.
> Em que posição ela apareceu a primeira vez.
> Em que posição ela apareceu a última vez.
'''

frase = str(input('Digite uma frase: ')).strip().upper()

#print('A letra A apareceu {} vezes na frase.'.format(frase.count('A')))

print(f'A letra A apareceu {frase.count("A")} vezes na frase')

print(f'A primeira letra A aparece na posição {frase.find("A") + 1}')

print(f'A última letra A aparece na posição {frase.rfind("A") + 1}')

