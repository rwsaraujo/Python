"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a US$ 1250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
[EN]
> Write a program that asks an employee's salary and calculates the amount of your raise. For salaries over US$ 1250.00,
calculate a 10% increase. For the lower or equal, the increase is 15%.
"""
salário = float(input('Salário: US$ '))
if salário > 1250:
    novo_salário = salário + (salário * 10 / 100)
else:
    novo_salário = salário + (salário * 15 / 100)
print(f'O novo salário é de US$ {novo_salário:.2f}.')