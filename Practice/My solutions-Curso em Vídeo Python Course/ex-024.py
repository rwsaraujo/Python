"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
>Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "santo".
[EN]
> Create a program that reads the name of a city that tells you whether or not it starts with the name "saint".
"""
nome_cidade = str(input('Nome da cidade: ')).upper().strip()
if nome_cidade[0:5] == 'SANTO':
    print('Existe a palavra "santo" no nome da cidade!')
else:
    print('Não existe a palavra "Santo" no começo do nome da cidade!')