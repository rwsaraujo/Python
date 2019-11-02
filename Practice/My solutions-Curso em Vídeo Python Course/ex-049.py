"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
[EN]
> Redo CHALLENGE 009, showing the multiplication table of a number that the user chooses, only now using a for loop.
"""
num = int(input('Digite um número para ver a tabuada: '))
for k in range(1, 11):
    print(f'{num} x {k} = {num * k}')