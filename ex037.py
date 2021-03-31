'''
DESAFIO 037

Escreva um programa que leia um número inteiro e peça para usuário escolher
qual será a base de conversão:
1 BINÁRIO  
2 OCTAL
3 HEXADECIMAL
'''

num = int(input('Digite um número inteiro: '))

escolha =  int(input( '''Escolha a base de conversão desejada:
[1] Para binário
[2] Para octal
[3] Para hexadecimal
Sua opção: '''))

if escolha == 1:
    print(f'O número {num} convertido para binário é: ',bin(num)[2:])

elif escolha == 2:
    print(f'O número {num} convertido para octal é: ',oct(num)[2:])

elif escolha == 3:
    print(f'O número {num} convertido para hexadecimal é: ',hex(num)[2:])

else:
    print('Opção inválida, tente novamente.')
