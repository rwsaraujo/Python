"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
[EN]
> Create a program that reads name, year of birth, and work card and records it (aged) in a dictionary. If CTPS happens
to be different from ZERO, the dictionary will also receive the year of hiring and the salary. Calculate and add, in
addition to age, how old the person will retire.
"""
#Gustavo Guanabara
""" from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
  dados['contratação'] = int(input('Ano de contratação: '))
  dados['salário'] = float(input('salário: R$ '))
  dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
  print(f' - {k} tem o valor {v}') """
  
