"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
[EN]
> Improve the game of CHALLENGE 028 where the computer will "think" on a number between 0 and 10. Only now the player
will try to guess until it hits, showing in the end how many guesses it took to win.
"""
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')