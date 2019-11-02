"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a
matriz na tela, com a formatação correta.
[EN]
> Create a program that declares a 3x3 dimension matrix and fills in values read by the keyboard. At the end, show the
matrix on the screen, with the correct formatting.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
  for c in range(0, 3):
    matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{matriz[l][c]:^5}]', end='')
  print()