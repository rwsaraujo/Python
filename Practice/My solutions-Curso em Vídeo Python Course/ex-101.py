"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
[EN]
> Create a program that has a function called vote () that will take as a parameter a person's year of birth, returning
a literal value indicating whether a person has DENIED, OPTIONAL, and REQUIRED votes in elections.
"""
def voto(ano):
  from datetime import date
  atual = date.today().year
  idade = atual - ano
  if idade < 16:
    return f'Com {idade} anos: NÃO VOTA.'
  elif 16 <= idade < 18 or idade > 65:
    return f'Com {idade} anos: VOTO OPICIONAL.'
  else:
    return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

# PROGRAMA PRINCIPAL
nasc = int(input('Em que ano você nasceu?'))
print(voto(nasc))