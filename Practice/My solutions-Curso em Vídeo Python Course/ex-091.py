"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
[EN]
> Create a program where 4 players roll a die and have random results. Store these results in a Python dictionary. In
the end, put this dictionary in order, knowing that the winner drew the highest number in the die.
"""
#Gustavo Guanabára
""" from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
  print(f'{k} tirou {v} no dado.')
  sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
  print(f'   {i + 1}º lugar: {v[0]} com {v[1]}.')
  sleep(1) """
