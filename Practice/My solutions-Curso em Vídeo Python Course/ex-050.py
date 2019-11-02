"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.
[EN]
> Develop a program that reads six integers and shows the sum of only those that are even. If the value you enter is
odd, disregard it.
"""
soma = 0
for k in range(1, 7):
    num = int(input('Digite um número inteiro qualquer: '))
    if num % 2 == 0:
        soma += num
print(f'A soma de todos os números pares entre os digitados é igual a {soma}.')
