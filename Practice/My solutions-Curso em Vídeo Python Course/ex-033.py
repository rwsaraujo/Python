"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
[EN]
> Make a program that reads three numbers and shows which is the largest and which is the smallest.
"""
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = int(input('Digite mais um número inteiro: '))
maior = num1
menor = num3
if maior < num2:
    maior = num2
if maior < num3:
    maior = num3
if menor > num2:
    menor = num2
if menor > num1:
    menor = num1
print(f'Maior: {maior}.')
print(f'Menor: {menor}.')