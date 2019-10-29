"""
NOME/NAME: Raphael Araújo
DATA/DATE: 29/10/2019NOME/NAME: Raphael Araújo
DATA/DATE: 29/10/2019
[PT]
> Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
[EN]
> Write a program that reads a value in meters and displays it converted to centimeters and millimeters.
"""
metros = float(input('Digite a medida (em metros): '))
centímetros = metros * 100
milímitros = metros * 1000
print(f'{metros} metro(s) é equivalente a {centímetros} centímetro(s) e equivalente a {milímitros} milímetros.')