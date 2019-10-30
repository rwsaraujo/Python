"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
> Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
mostre o comprimento da hipotenusa.
[EN]
> Make a program that reads the length of the opposite and adjacent sides of a right triangle. Calculate and show the
length of the hypotenuse.
"""
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hipotenusa:.2f}.')