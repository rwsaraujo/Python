"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
> Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
[EN]
> Make a program that reads from 0 to 9999 and displays each of the separate digits on the screen.
"""
# Leitura do número inteiro a partir do teclado
num = int(input('Informe um número: '))
# Método 1
n = str(num)
print(f'Análise do número {num}:')
print(f'Unidade: \t{n[3]}')
print(f'Dezena: \t{n[2]}')
print(f'Centena: \t{n[1]}')
print(f'Milhar: \t{n[0]}')
# Método 2
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
# Impressão do resultado
print(f'Análise do número {num}:')
print(f'Unidade: \t{u}')
print(f'Dezena: \t{d}')
print(f'Centena: \t{c}')
print(f'Milhar: \t{m}')