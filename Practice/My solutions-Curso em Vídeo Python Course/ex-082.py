"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas.
[EN]
> Create a program that will read multiple numbers and put in a list. After that, create two extra lists that will
contain only the even values and the odd values entered, respectively. At the end, show the contents of the three
generated lists.
"""
L = []
L_P = []
L_I = []
while True:
  L.append(int(input('Digite um número: ')))
  while True:
    resp = str(input('Quer continuar (S/N)? ')).upper().strip()
    if resp == 'S' or resp == 'N':
      break
    else:
      print('Resposta inválida!')
  if resp == 'N':
    break
  
#Gerar duas listas (uma de pares, outra de ímpares) a partir de uma lista 
for k in range(0, len(L)):
  if L[k] % 2 == 0:
    L_P.append(L[k])
  else:
    L_I.append(L[k])

#Outra forma de gerar duas lista a partir de outra:
'''
for x, k in enumerate(L):
  if k % 2 == 0:
    L_P.append(k)
  elif k % 2 == 1:
    L_I.append(k)
'''
    
print(f'Todos os números digitados:{L}')
print(f'Todos os números pares digitados:{L_P}')
print(f'Todos os números ímpares digitados:{L_I}')