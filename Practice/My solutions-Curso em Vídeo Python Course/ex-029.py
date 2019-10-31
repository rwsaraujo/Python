"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
foi multado. A multa vai custar US$ 7,00 por cada Km acima do limite.
[EN]
> Write a program that reads the speed of a car. If it exceeds 80km/h, display a message saying that it has been fined.
The fine will cost US$ 7,00 for each Km above the limit.
"""
velocidade = float(input('Velocidade do veículo (km/h): '))
if velocidade > 80:
    print('Você excedeu o limite de velocidade de 80km/h.')
    print(f'Você foi multado por excesso de velocidade! \nValor da multa: US$ {(velocidade - 80) * 7:.2f}')
else:
    print('Tenha um bom dia! Dirija com segurança.')