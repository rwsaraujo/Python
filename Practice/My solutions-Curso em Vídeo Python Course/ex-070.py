"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
[EN]
> Crie um programa que leia o nome e o preço de vários produtos. O programa solicita que o usuário continue ou não. No
final, mesquita:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R $ 1000.
C) qual é o nome do produto mais barato.
"""
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: US$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi US$ {total:.2f}.')
print(f'Temos {totmil} produtos custando mais de US$ 1000.00.')
print(f'O produto mais barato foi <{barato.upper()}> que custa US$ {menor:.2f}.')