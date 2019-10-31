"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
>  Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
[EN]
> Write a Python program that reads any integer and asks the user to choose what the conversion base will be: 1 for
binary, 2 for octal and 3 for hexadecimal.
"""
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das base para conversão:
        [1] converter para BINÁRIO
        [2] converter para OCTAL
        [3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}.')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}.')
elif opção == 3:
    print(f'convertido para HEXADECIMAL é igual a {hex(num)[2:]}.')
else:
    print('Opção inválida. Tente novamente.')