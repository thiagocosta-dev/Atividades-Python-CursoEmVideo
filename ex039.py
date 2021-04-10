'''
DESAFIO 039

Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que fala ou que passou do prazo.
'''

from datetime import date

ano_atual = date.today().year
nascimento = int(input('Qual o ano do seu nascimento: '))
idade = ano_atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} em {ano_atual}')

if idade == 18:
    print(f'Você precisa se alistar imediatamente!')

elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} ano(s) para se alistar.')
    ano = ano_atual + saldo
    print(f'Seu alistamento será em {ano}')
else:
    saldo = idade - 18
    print(f'Você deveria ter se alistado há {saldo} ano(s).')
    ano = ano_atual - saldo
    print(f'Seu alistamento foi em {ano}')
