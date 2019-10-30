"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
> Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
nome dos alunos e escrevendo na tela o nome do escolhido.
[EN]
> A teacher wants to raffle one of his four students to erase the board. Make a program that helps him by reading the
students' names and writing the name of the chosen one on the screen.
"""
from random import choice
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}.')