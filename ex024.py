'''

Crie um programa que leia o nome de uma cidade e diga se ela começa
com a palavra 'SANTO'.
'''

cid= str(input('Digite a cidade que você nasceu: ')).upper().strip()

print(cid[:5] == 'SANTO')

