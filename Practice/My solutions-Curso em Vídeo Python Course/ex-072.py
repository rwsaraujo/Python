"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu
programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
[EN]
> Create a program that has a fully populated tuple with a full count from zero to twenty. Your program should read a
number from the keyboard (between 0 and 20) and show it in full.
"""
cont_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
                    'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
                    'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
                    'dezenove', 'vinte')
while True:
  num = int(input('Digite um número inteiro entre 0 e 20: '))
  if -1 < num < 21:
    print(f'{num} escrito por extenso: {cont_por_extenso[num]}.')
    break
  else:
    print('Número inválido!')