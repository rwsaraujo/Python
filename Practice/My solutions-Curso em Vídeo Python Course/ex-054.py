"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
maioridade e quantas já são maiores.
[EN]
> Create a program that reads the birth year of seven people. In the end, show how many people are not yet of age and
how many are older.
"""
from datetime import date
ano_atual = date.today().year
maiores = 0
menores = 0
for k in range(1, 8):
    ano_nasc = int(input(f'Ano de nascimento da pessoa {k}:'))
    if ano_atual - ano_nasc > 18:
        maiores += 1
        print('É maior de idade!')
    else:
        menores += 1
        print('É menor de idade!')
print(f'O número de pessoas maiores de idade é igual a {maiores}.')
print(f'O números de pessoas menores de idade é igual a {menores}.')