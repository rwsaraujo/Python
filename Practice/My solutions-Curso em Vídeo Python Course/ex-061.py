"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma Progressão Aritmética, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
[EN]
> Redo CHALLENGE 051 by reading the first term and the reason for an Arithmetic Progression, showing the first 10 terms
of the progression using the while structure.
"""
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razão
    cont += 1
print('FIM')