'''
DESAFIO 049

Refaça o exercício 09, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando laço for.
'''

num = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    print(f'{num} x {c:2} = {num * c:2}')
