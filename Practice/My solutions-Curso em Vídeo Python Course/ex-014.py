"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
> Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
[EN]
> Write a program that converts a temperature by typing in degrees Celsius and converts it to degrees Fahrenheit.
"""
temp_c = float(input('Informe a temperatura em °C: '))
temp_f = 9 * temp_c / 5 + 32
print(f'A temperatura de {temp_c:.2f}°C corresponde a {temp_f:.2f}°F.')