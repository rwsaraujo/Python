"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
> Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
[EN]
> Create a program that reads how much money a person has in their wallet and shows how many dollars they can buy.
"""
reais = float(input('Dinheiro na sua carteira (R$): '))
# Supondo que no dia da conversão 1 dólar = 4 reais
print(f'Com R${reais:.2f} você pode compra US${reais / 4:.2f}.')