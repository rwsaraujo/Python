"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
- Até 9 anos: MIRIM.
- Até 14 anos: INFANTIL.
- Até 19 anos: JÚNIOR.
- Até 25 anos: SÊNIOR.
- Acima de 25 anos: MASTER.
[EN]
> The National Swimming Confederation needs a program that reads an athlete's birth year and shows its category
according to age:
- Up to 9 years old: MIRIM.
- Up to 14 years old: CHILD.
- Up to 19 years old: JR.
- Up to 25 years old: SENIOR.
- Over 25 years: MASTER.
"""
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
if idade <= 9:
    print('A categoria do atleta é MIRIM.')
elif idade <= 14:
    print('A categoria do atleta é INFANTIL.')
elif idade <= 19:
    print('A categoria do atleta é JÚNIOR.')
elif idade <= 25:
    print('A categoria do atleta é SÊNIOR.')
else:
    print('A categoria do atleta é MASTER.')