'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO

'''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

print(f'Tirando a nota {n1:.1} e {n2:.1f}, a média é {media}.')

if media < 5:
    print(f'O aluno está REPROVADO.')

elif media >= 7:
    print('O aluno está APROVADO.')

else:
    print('O alune está em RECUPERAÇÃO.')
