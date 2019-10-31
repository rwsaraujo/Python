"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
>  Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
[EN]
> Create a program that reads an integer and shows on the screen whether it is even or odd.
"""
num = int(input('Digite um número inteiro qualquer: '))
if num % 2 == 0:
    print('O número é par!')
else:
    print('O número é ímpar!')