"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um
valor monetário formatado.
[EN]
> Adapt challenge code # 107 by creating an additional function called currency () that can display the numbers as a
formatted monetary value.
"""
import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')