"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
> Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
[EN]
> Make a program that reads any angle and shows the sine, cosine, and tangent value of that angle on the screen.
"""
from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print(f'A ângulo de {ângulo} tem o SENO de {seno:.2f}.')
cosseno = cos(radians(ângulo))
print(f'O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}.')
tangente = tan(radians(ângulo))
print (f'O ângulo de {ângulo} tem a TANGENTE de {tangente:.2f}.')