"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza (primeiro = Ana; último = Souza).
[EN]
>Make a program that reads a person's full name, then shows the first and last name separately.
Ex: Ana Maria de Souza (first = Ana; last = Souza).
"""
nome = str(input('Digite o nome completo: ')).strip().split()
print(f'Primeiro nome: \t{nome[0]}.')
print(f'Último nome: \t{nome[-1]}.')