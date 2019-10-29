"""
NOME/NAME: Raphael Araújo
DATA/DATE: 29/10/2019
[PT]
> Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
[EN]
> Develop a program that reads a student's two grades, calculates and shows their average.
"""
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print(f'A média do aluno é igual a {média:.1f}.')
