'''
DESAFIO 041

Crie um programa que leia o ano de nascmento de um atleta.
e mostre sua categoria,de acordo com a idade:
- Até 9 anos: MIRIM     - Até 25 anos: SÊnior
- Até 14 anos: INFANTIL - Acima: MASTER
- Até 19 anos: JUNIOR
'''
from datetime import date
ano_atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano_atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {ano_atual}')
if idade <= 9:
    print(f'Categoria: MIRIM.')
elif idade <= 14:
    print(f'Categoria: INFANTIL.')
elif idade <= 19:
     print(f'Categoria: JUNIOR.')
elif idade <= 25:
     print(f'Categoria: SÊNIOR.')
else:
     print(f'Categoria: MASTER.')
