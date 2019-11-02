"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
(desconsiderando o flag).
[EN]
> Create a program that reads whole numbers on the keyboard. The program will only stop when the user enters the value
999, which is the stop condition. At the end, show how many numbers were typed and what was the sum between them
(disregarding the flag).
"""
soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos valores foi {soma}.')