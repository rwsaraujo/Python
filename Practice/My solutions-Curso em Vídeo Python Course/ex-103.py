"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.
[EN]
> Make a program that has a function called chip (), which takes two optional parameters: a player's name and how many
goals he has scored. The program should be able to display the player's record even if some data has not been entered
correctly.
"""
def ficha(n='<desconhecido>', g=0):
  print(f'Nome do jogador: {n}')
  print(f'Gols marcados: {g}')


#Programa principal
nome = str(input('Nome do jogador: '))
q_gols = str(input('Gols marcados: '))
if q_gols.isnumeric():
  q_gols = int(q_gols)
else:
  q_gols = 0
if nome.strip() == '':
  ficha(g = q_gols)
else:
  ficha(nome, q_gols)