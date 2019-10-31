"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:
- à vista dinheiro/cheque: 10% de desconto.
- à vista no cartão: 5% de desconto.
- em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.
[EN]
> Design a program that calculates the amount to be paid for a product, considering its normal price and payment
condition:
- Cash / Check: 10% off.
- cash on the card: 5% off.
- up to 2x on the card: normal price.
- 3x or more on the card: 20% interest.
"""
preço = float(input('Preço: US$ '))
opção_pag = int(input('''FORMA DE PAGAMENTO:
        [1] - À VISTA/CHEQUE:    10% DE DESCONTO
        [2] - À VISTA NO CARTÃO: 5% DE DESCONTO
        [3] - 2x NO CARTÃO:      PREÇO NORMAL
        [4] - 3x NO CARTÃO:      20% DE JUROS
---> '''))
if opção_pag == 1:
    preço_final = preço - (preço * 10 / 100)
    print(f' O preço final com desconto de 10% é de US$ {preço_final:.2f}.')
elif opção_pag == 2:
    preço_final = preço - (preço * 5 / 100)
    print(f'O preço final com desconto de 5% é de US$ {preço_final:.2f}.')
elif opção_pag == 3:
    print(f'O preço final é de US$ {preço:.2f}.')
elif opção_pag == 4:
    preço_final = preço + (preço * 20 / 100)
    print(f'O preço final com juros de 20% é de US$ {preço_final:.2f}.')