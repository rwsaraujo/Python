"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente.
[EN]
> Create a program where the user can enter multiple numeric values and enter them in a list. If the number already
exists inside, it will not be added. At the end, all unique values entered will be displayed in ascending order.
"""
L = []
num = int(input('Digite um número: '))
while True:  
  if num in L:
    print('Esse número já existe! ')    
  else:
    L.append(num)
  resp = ' '
  while resp not in 'SN':
    resp = str(input('Deseja continuar (S/N)? ').upper().strip())
    if resp != 'S' and resp != 'N':
      print('Resposta inválida!')
      resp = ' '
  if resp == 'N':
    break
  num = int(input('Digite um novo número: '))
print(f'Valores digitados em ordem crescente: {sorted(L)}')