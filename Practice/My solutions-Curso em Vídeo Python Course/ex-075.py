"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
[EN]
> Develop a program that reads four values from the keyboard and saves them in a tuple. At the end, show:

A) How many times did the value 9 appear.
B) At what position was entered the first value 3.
C) What were the even numbers.
"""
nove = 0
pos_três = -1
par = [-1]
valores = [0, 0, 0, 0]
for p in range(0, 4):
  valores[p] = int(input('Digite um valor qualquer: '))

valores_t = (valores[0], valores[1], valores[2], valores[3])
             
for p in range(0, len(valores_t)):
  if valores_t[p] == 9:
    nove += 1
  if pos_três == -1 and valores_t[p] == 3:
    pos_três = p
  if valores_t[p] % 2 == 0:
    par.append(valores_t[p])

print(f'O nove apareceu {nove}x.')

if pos_três > -1:
  print(f'O valor 3 apareceu primeiro na posição {pos_três + 1}.')
    
if len(par) > 1:
  print(f'Pares: {par[1:]}.')

'''#Solução do Gustavo Guanabara:
núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {valores_t.count(9)}x.')
if 3 in valores_t:
  print(f'O valor 3 apareceu na posição {valores_t.index(3) + 1}')
else:
  print('o valor 3 não foi digitado em nenhuma posição')
print('os valores pares digitados foram ', end='')
for n in núm:
  if n % 2 == 0:
    print(n, end=' ')'''