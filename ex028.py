'''
DESAFIO 028

Escreva um program que faça o computador 'pensar' em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi número escolhido
. O programa deve escrever na tela se uauário venceu ou perdeu
'''

from random import randint as rd
from time import sleep as sl

numPC = rd(0, 5)

numUSU = int(input('Acerte o número: '))

print('PROCESSANDO...')
sl(2)

if numPC == numUSU:
    print(f'PARABÉNS! Você acertou!! Eu pensei no {numUSU}.')

else:
    print(f'ERROU!! Pensei no número {numPC} e não no {numUSU}.')

