"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
[EN]
> Write a program that makes the computer "think" an integer between 0 and 5 and ask the user to try to figure out what
number the computer chose. The program should write on the screen if the user has won or lost.
"""
import random
num = [0, 1, 2, 3, 4, 5]
n = random.choice(num)
escolha = int(input('O computador escolheu um número de 0 a 5. Tente acertar qual foi: '))
if escolha >= 0 and escolha <= 5:
    if escolha == n:
        print(f'Você venceu!!! O computador escolheu o número {n}.')
    else:
        print(f'Você perdeu!!! O computador escolheu o número {n}.')
else:
    print('Número inválido!')