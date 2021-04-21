'''
Faça um programa que leia um  número inteiro e diga se ela é ou não um número primo.

'''

num = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[33m', end=' ')
        total = total + 1
    else:
        print('\33[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {total} vezes.')
if total == 2:
    print('É número primo.')
else:
    print('Não é número primo.')
