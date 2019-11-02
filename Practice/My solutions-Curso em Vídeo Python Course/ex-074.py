"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla.
[EN]
> Create a program that will generate five random numbers and put in a tuple. After that, show the list of generated
numbers and also enter the smallest and largest values that are in the tuple.
"""
from random import randint

t = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(t)

'''maior = 0
menor = 100
for p in range(0, len(t)):
  if maior < t[p]:
    maior = t[p]
  if menor > t[p]:
    menor = t[p]
    
print(f'O maior é o {maior}.')
print(f'O menor é o {menor}.')'''

print(f'O maior valor é {max(t)}')
print(f'O menor valor é {min(t)}')


