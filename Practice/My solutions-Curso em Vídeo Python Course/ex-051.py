"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética. No final, mostre os 10
primeiros termos dessa progressão.
[EN]
> Develop a program that reads the first term and the reason for an Arithmetic Progression. In the end, show the first
10 terms of this progression.
"""
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(f'{c} ', end='-> ')
print('ACABOU')