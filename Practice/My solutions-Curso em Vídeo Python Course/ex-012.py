"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
> Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
[EN]
> Make an algorithm that reads the price of a product and shows its new price at 5% off.
"""
preço = float(input('Preço: US$ '))
preço_desc = preço - (preço * 5 / 100)
print(f'Preço com desconto de 5%: US$ {preço_desc:.2f}.')