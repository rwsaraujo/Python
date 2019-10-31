"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
[EN]
> Create a program that reads two grades from a student and averages them, showing a message at the end, according to
the average achieved:
- Average below 5.0: FAILED.
- Average between 5.0 and 6.9: RECOVERY.
- Average 7.0 or higher: OK.
"""
nota1 = float(input('Primeira nota: \t'))
nota2 = float(input('Segunda nota: \t'))
média = (nota1 + nota2) / 2
print(f'A média no aluno é {média:.1f}.')
if média > 7:
    print('Aluno APROVADO!')
elif 5 <= média < 7:
    print('Aluno em RECUPERAÇÃO!')
else:
    print('Aluno REPROVADO!')