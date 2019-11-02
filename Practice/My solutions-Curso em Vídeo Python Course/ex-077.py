"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.
[EN]
> Create a program that has a multiple word tuple (no accents). After that you should show, for each word, what your
vowels are.
"""
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
  print(f'\nNa palavra {p.upper()} temos ', end='')
  for letra in p:
    if letra.lower() in 'aeiou':
      print(letra, end=' ')