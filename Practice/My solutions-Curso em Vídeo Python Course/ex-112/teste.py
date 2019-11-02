"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas
valores que seja monetários.
[EN]
> Within the utilitiesCeV package we created in challenge 111, we have a module called data. Create a function called
readMoney () that can function as the impute () function, but with data validation to accept only monetary values.
"""
from des112.utilidadescev import moeda
from des112.utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)