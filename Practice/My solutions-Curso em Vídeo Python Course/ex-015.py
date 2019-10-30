"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
> Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias que ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
[EN]
> Write a program that asks how many miles a rental car has traveled and how many days it has been rented. Calculate
the price to pay knowing that the car costs $ 60 per day and $ 0.15 per km driven.
"""
km_percorridos = float(input('Quantidade de Km percorridos: '))
dias_aluguel = int(input('Dias de aluguel: '))
preço_total = (dias_aluguel * 60) + (km_percorridos * 0.15)
print(f'O preço do aluguel é de US$ {preço_total:.2f}.')