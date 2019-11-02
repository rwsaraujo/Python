"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.
[EN]
> Make a program that will display a countdown to the fireworks burst, going from 10 to 0, with a 1 second pause
between them.
"""
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('BUM! BUM! POW!')

