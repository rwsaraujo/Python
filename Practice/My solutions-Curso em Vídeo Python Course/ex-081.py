"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
[EN]
> Create a program that will read multiple numbers and put in a list. After that, show:
A) How many numbers have been entered.
B) The list of values, sorted in descending order.
C) Whether the value 5 has been entered and is or is not in the list.
"""
L = []
while True:
  L.append(int(input('Digite um número: ')))
  while True:
    resp = str(input('Deseja continuar (S/N)? ')).upper().strip()
    if resp == 'S' or resp == 'N':
      break
    else:
      print('Resposta inválida!')
  if resp == 'N':
    break
print(f'Quantidade de números digitados: {len(L)}')
L.sort(reverse = True)
print(L)
if 5 in L:
  print('O valor 5 foi digitado!')
else:
  print('O valor 5 não foi digitado e está na lista!')