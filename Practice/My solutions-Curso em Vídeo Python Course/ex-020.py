"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
> O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
leia o nome dos quatro alunos e mostre a ordem sorteada.
[EN]
> The same teacher of challenge 019 wants to draw the order of presentation of students. Make a program that reads the
names of the four students and shows the order drawn.
"""
from random import shuffle
nome1 = str(input('Primeiro aluno:'))
nome2 = str(input('Segundo aluno:'))
nome3 = str(input('Terceiro aluno:'))
nome4 = str(input('Quarto aluno:'))
turma = [nome1, nome2, nome3, nome4]
shuffle(turma)
print(f'A ordem de apresentação será: \n-> {turma}')