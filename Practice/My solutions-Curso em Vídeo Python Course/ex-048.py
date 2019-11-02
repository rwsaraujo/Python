"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo
de 1 até 500.
[EN]
> Make a program that calculates the sum of all numbers that are multiples of three and in the range 1 to 500.
"""
s = 0
for c in range(0, 500):
    if c % 2 != 0:
        if c % 3 == 0:
            s += c
print(f'A soma de todos os inteiros ímpares que são múltiplos de 3, de 1 a 500, é igual a {s}.')

