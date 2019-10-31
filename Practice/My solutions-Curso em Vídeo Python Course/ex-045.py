"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> Crie um programa que faça o computador jogar Jokenpô com você.
[EN]
> Create a program that makes the computer play Jokenpô with you.
"""
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
while True:
    jogador = int(input('Qual é a sua jogada? '))
    if 0 <= jogador <= 2:
        break
    else:
        print('JOGADA INVÁLIDA!')
print('-=' * 11)
print(f'Computador jogou {itens[computador]}.')
print(f'Jogador jogou {itens[jogador]}.')
print('-=' * 11)
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')