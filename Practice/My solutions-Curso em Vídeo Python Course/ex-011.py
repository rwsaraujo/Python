"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
> Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
[EN]
> Make a program that reads the width and height of a wall in meters, calculates its area and the amount of paint
needed to paint it, knowing that every liter of paint paints an area of 2 square meters.
"""
largura = float(input('Digite a largura da parede (em metros): '))
altura = float(input('Digite a altura da parede (em metros): '))
área = largura * altura
print(f'Com {largura}m de largura e {altura}m de altura, a parede tem {área}m² de área.')
print(f'Você precisará de pelo menos {área / 2:.1f}lts de tinta para pintar a parede.')