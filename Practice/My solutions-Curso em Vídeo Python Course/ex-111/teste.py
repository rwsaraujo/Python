"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
>  Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as
funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
[EN]
> Create a package called utilitiesCeV that has two built-in modules called currency and dice. Transfer all the
functions used in challenges 107, 108, and 109 to the first package and keep it running.
"""
from des111.utilidadescev import moeda

p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 35, 22)