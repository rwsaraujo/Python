"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo
de cálculo do fatorial.
[EN]
> Create a program that has a factorial function () that takes two parameters: the first one that indicates the number
to calculate and another called show, which will be a logical value (optional) indicating whether or not the factorial
calculation process will be shown on the screen. .
"""
def fatorial(n, show=False):
  f = 1
  for c in range(n, 0, -1):
    if show:
      print(c, end='')
      if c > 1:
        print(' x ', end='')
      else:
        print(' = ', end='')
    f *= c
  return f


#Programa principal
print(fatorial(5, show=True))
