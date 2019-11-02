"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de
tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
[EN]
> Rewrite the readInt () function we did in challenge 104, now including the possibility of typing an invalid type
number. Enjoy and also create a readFloat () function with the same functionality.
"""
def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n

def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = LeiaInt('Digite um valor Inteiro: ')
n2 = LeiaFloat('Digite um valor Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
