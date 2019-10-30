"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
> Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
[EN]
> Create a program that reads a person's full name and shows:
- The name with all uppercase and lowercase letters.
- How many letters in all (regardless of spaces).
- How many letters has the first name.
"""
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome.lower()}.')
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))