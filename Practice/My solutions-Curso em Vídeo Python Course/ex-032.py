"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> Faça um programa que leia um ano qualquer e mostre se ele é um ano bissexto.
[EN]
> Make a program that reads any year and shows if it is a leap year.
"""
from datetime import date
ano = int(input('Digite um ano qualquer para saber se ele é um ano bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')