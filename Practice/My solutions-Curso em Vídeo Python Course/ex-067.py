"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
programa será interrompido quando o número solicitado for negativo.
[EN]
> Make a program that shows the multiplication table, one at a time, for each value entered by the user. The program
will be interrupted when the requested number is negative.
"""
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCRRADO. VOLTE SEMPRE!')
