"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
comprimento) e mostre a área do terreno.
[EN]
> Make a program that has a function called area (), which takes the dimensions of a rectangular terrain (width and
length) and shows the terrain area.
"""
def área(l, c):
  print(f'A área do terreno é igual a {l * c}m².')

#Programa principal
print('Digite abaixo as medidas do terreno: ')
ml = float(input('Largura >>> '))
mc = float(input('Comprimento >>> '))
área(ml, mc)