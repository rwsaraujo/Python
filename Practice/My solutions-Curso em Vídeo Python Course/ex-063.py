"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência
de Fibonacci.
[EN]
> Write a program that reads any integer N and shows the first N elements of a Fibonacci Sequence on the screen.
"""
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~' * 30)