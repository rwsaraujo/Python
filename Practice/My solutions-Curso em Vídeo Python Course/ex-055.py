"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
[EN]
> Make a program that reads the weight of five people. In the end, show which was the highest and lowest weight read.
"""
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg.')
print(f'O menor peso lido foi de {menor}Kg.')