"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo
será negado.
[EN]
> Write a program to approve the bank loan for the purchase of a home. Ask the value of the house, the buyer's salary
and how old he will pay. The monthly installment cannot exceed 30% of the salary or else the loan will be denied.
"""
casa = float(input('Valor da casa: US$ '))
salário = float(input('Salário do comprador US$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
print(f'Para pagar uma casa de US$ {casa:.2f} em {anos} anos...')
print(f'A prestação será de US$ {prestação:.2f}.')
print(f'30% do salário do comprador: US$ {(salário / 100) * 30:.2f}.')
if prestação <= (salário / 100) * 30:
    print('Prestação mensal abaixo de 30% do salário do comprador. \nEmpréstimo concedido.')
    print(f'30% do salário do comprador: US$ \033[32m{(salário / 100) * 30:.2f}.')
else:
    print(f'Prestação mensal acima de 30% do salário do comprador. \nEmpréstimo negado.')
    print(f'30% do salário do comprador: US$ \033[31m{(salário / 100) * 30:.2f}.')