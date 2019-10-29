"""
NOME/NAME: Raphael Araújo
DATA/DATE: 29/10/2019
[PT]
> Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
[EN]
> Make a program that reads something from the keyboard and displays its primitive type and all possible information about it.
"""
algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(algo)}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'E alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minúsculas? {algo.islower()}')