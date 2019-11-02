"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de US$50, US$20, US$10 e US$1.
[EN]
> Create a program that simulates the operation of an ATM. At the beginning, ask the user what will be the amount to be
withdrawn (integer) and the program will inform how many banknotes of each amount will be delivered.
NOTE: Consider that the cashier has banknotes of US$50, US$20, US$10 and US$1.
"""
print('=' * 30)
print('{:^30}'.format('BANCO ARAÚJO'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? \n---> US$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de US$ {céd}.')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO ARAÚJO! Tenha um bom dia!')