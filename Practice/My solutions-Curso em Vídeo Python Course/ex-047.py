"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
[EN]
> Create a program that displays all even numbers that are in the range 1 to 50 on the screen.
"""
for intervalo in range(0, 51):
    if intervalo % 2 == 0:
        print(intervalo)