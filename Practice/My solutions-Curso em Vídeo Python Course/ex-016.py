"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
> Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
[EN]
> Create a program that reads any Real Number on the keyboard and shows its Integer portion on the screen.
"""
num = float(input('Digite um número Real qualquer (Ex.: 1.598): \n-> '))
print(f'A parte inteira do número {num} é {int(num)}.')