"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular.
[EN]
> Create a program that has a unique tuple with product names and their prices, in sequence. At the end, show a price
listing, organizing the data in tabular form.
"""
info = ('mouse', 70,
        'teclado', 150,
        'monitor', 500)
print('-' * 40)
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print('-' * 40)
for pos in range(0, len(info)):
  if pos % 2 == 0:
    print(f'{info[pos]:.<30}', end='')
  else:
    print(f'R${info[pos]:>7.2f}')
print('-' * 40)