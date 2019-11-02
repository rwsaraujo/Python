"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
[EN]
> Develop a program that reads the name, age and gender of 4 people. At the end of the program, show: the average age
of the group, what is the name of the oldest man and how many women are under 20 years old.
"""
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ' '
totmulher20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 + 1        
médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade}.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
