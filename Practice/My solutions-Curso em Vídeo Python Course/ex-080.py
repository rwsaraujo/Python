"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
[EN]
> Create a program where the user can type five numeric values and enter them in a list, already in the correct
insertion position (without using sort ()). At the end, show the ordered list on the screen.
"""
L = []
while True:
  if len(L) < 5:
    num = int(input('Digite um número inteiro qualquer: '))
    if num in L:
      L.insert(L.index(num), num)
    elif len(L) < 1:
      L.append(num)
    else:
      k = 0
      while True:          
        if num < L[k]:
          L.insert(L.index(L[k]), num)
          break
        else:
          if k < len(L):
            k += 1
            if k == len(L):
              L.append(num)
              k += 1
        if k == len(L):
          break
  else:
    break
print(L)


#Gustavo Guanabara
'''
lista = []
for c in range(0, 5):
  n = int(input('Digite um valor: '))
  if c == 0 or n > lista[-1]:
    lista.append(n)
  else:
    pos = 0
    while pos < len(lista):
      if n <= lista[pos]:
        lista.insert(pos, n)
        break
      pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
'''

