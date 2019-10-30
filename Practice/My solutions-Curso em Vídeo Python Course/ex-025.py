"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
> Crie um programa que leia o nome de uma pessoa e diga se ela tem "Araújo" no nome.
[EN]
> Create a program that reads a person's name and tells them if they have "Araújo" in their name.
"""
nome = str(input('Nome completo: ')).strip().upper()
if 'ARAUJO' in nome or 'ARAÚJO' in nome:
    print('Existe "Araújo"/"Araujo" no nome.')
else:
    print('Não existe "Araújo"/"Araujo" no nome.')