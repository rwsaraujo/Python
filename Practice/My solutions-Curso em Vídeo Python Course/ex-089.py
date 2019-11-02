"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
[EN]
> Create a program that reads the name and two notes of several students and saves everything in a composite list. At
the end, show a grade card containing the average of each and allow the user to show each student's grades individually.
"""
ficha = list()
while True:
  nome = str(input('Nome: '))
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))
  media = (nota1 + nota2) / 2
  ficha.append([nome, [nota1, nota2], media])
  resp = str(input('Quer continuar? [S/N] '))
  if resp in 'Nn':
    break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
  print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
  print('-' * 35)
  opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
  if opc == 999:
    print('FINALIZANDO...')
    break
  if opc <= len(ficha) - 1:
    print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
