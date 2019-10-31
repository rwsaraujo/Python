"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
>  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela
aparece a primeira vez e em que posição ela aparece a última vez.
[EN]
> Make a program that reads a sentence on the keyboard and shows how often the letter "A" appears, where it appears the
first time, and where it last appears.
"""
frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase.'.format(frase.count("A")))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(frase.find('A') + 1))
print('A letra "A" aparece pela última vez na posição {}.'.format(frase.rfind("A") + 1))