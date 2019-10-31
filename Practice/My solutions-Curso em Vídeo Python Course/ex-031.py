"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando US$ 0.50
por Km para viagens de até 200Km e US$ 0.45 parta viagens mais longas.
[EN]
> Develop a program that asks for the distance of a trip in Km. Calculate the price of the ticket, charging US$ 0.50
per Km for trips up to 200Km and US$ 0.45 for longer trips.
"""
distância = float(input('Distância da viagem (km): '))
if distância <= 200:
    print(f'Preço da passagem US$ {distância * 0.5:.2f}.')
else:
    print(f'Preço da passagem US$ {distância * 0.45:.2f}')