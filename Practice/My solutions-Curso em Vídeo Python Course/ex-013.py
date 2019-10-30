"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
> Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
[EN]
> Write an algorithm that reads an employee's salary and shows his new salary, with a 15% increase.
"""
salário = float(input('Salário: US$ '))
salário_aumento = salário + (salário * 15 / 100)
print(f'O novo salário com aumento de 15% é de US$ {salário_aumento:.2f}.')