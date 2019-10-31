"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
[EN]
> Write a program that reads two integers and compares them. showing a message on the screen:
- The first value is higher.
- The second value is higher.
- There is no higher value, both are equal.
"""
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O PRIMEIRO número é o maior.')
elif num1 < num2:
    print('O SEGUNDO número é o maior. ')
else:
    print('Os dois números são iguais.')