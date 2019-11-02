"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
[EN]
> Create a tuple filled with the top 20 places on the Brazilian Football Championship Table, in order of placement. Then show:
a) The first 5 teams.
b) The last 4 placed.
c) Teams in alphabetical order.
d) What position is the Chapecoense team in?
"""
classif_br = ('Flamengo', 'Palmeiras', 'Santos', 'Corinthians', 'São Paulo',
              'Internacional', 'Grêmio', 'Bahia', 'Athletico-PR', 'Goiás',
              'Vasco da Gama', 'Atlético', 'Botafogo', 'Fluminense', 'Fortaleza',
              'Ceará SC', 'CSA', 'Cruzeiro', 'Avaí', 'Chapecoense')
print('Cinco primeiros colocados na tabela do Brasileirão 2019 até a 26º rodada:')
for p in range(0, 5):  
  print(f'{p + 1}º {classif_br[p]}')
print(' \n ')

print('Quatro últimos colocados na tabela do Brasileirão 2019 até a 26º rodada:')
for p in range(16, 20):
  print(f'{p + 1}º {classif_br[p]}')
print(' \n ')

print('Times da 1º Divisão do Brasileirão 2019 em ordem alfabética:')
for p in range(0, 20):
  print(f'{sorted(classif_br)[p]}')
print(' \n ')

for p in range(0, 20):
  if classif_br[p] == 'Chapecoense':
    print(f'A {classif_br[p]} está na {p + 1}º posição.')
print(' \n ')