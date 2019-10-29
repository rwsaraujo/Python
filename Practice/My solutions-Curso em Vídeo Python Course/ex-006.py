"""
NOME/NAME: Raphael Araújo
DATA/DATE: 29/10/2019
[PT]
> Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
[EN]
> Create an algorithm that reads a number and shows its double, triple, and square root.
"""
import math
num = int(input('Digite um número inteiro: '))
print(f'O dobro de {num} é {num * 2}.')
print(f'O triplo de {num} é {num * 3}.')
print(f'A raiz quadrada de {num} é {math.sqrt(num)}.')  # num**(1 / 2)
