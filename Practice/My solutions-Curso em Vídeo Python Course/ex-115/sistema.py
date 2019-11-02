"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Vamos criar um menu em Python, usando modularização.
[EN]
> Let's create a Python menu using modularization.
"""
from des115.lib.interface import *

while True:
    resposta = menu(['Ver pessias cadastradas', 'Cadastrar Pessoas', 'Sair so Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digit uma opção válida!')