"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça
também um programa que importe esse módulo e use algumas dessas funções.
[EN]
> Create a module called currency.py that has the built-in functions increase (), decrease (), double (), and half ().
Also make a program that imports this module and use some of these functions.
"""
import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
