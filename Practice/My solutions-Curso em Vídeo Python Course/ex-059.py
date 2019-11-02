"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
[EN]
> Create a program that reads two values and shows a menu on the screen:
[1] add
[2] multiply
[3] largest
[4] new numbers
[5] quit the program
Your program should perform the requested operation in each case.
"""
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1  + n2
        print(f'A soma {n1} + {n2} é igual a {soma}.')
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é igual a {produto}.')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}.')
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    print('=-=' * 10)
print('Fim do programa! Volte sempre.')