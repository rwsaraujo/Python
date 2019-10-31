"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso.
- Entre 18,5 e 25: Peso Ideal.
- 25 até 30: Sobrepeso.
- 30 até 40: Obesidade.
- Acima de 40: Obesidade Mórbida.
[EN]
> Develop a logic that reads a person's weight and height, calculates their Body Mass Index (BMI), and shows their
status according to the table below:
- BMI below 18.5: Underweight.
- Between 18.5 and 25: Ideal Weight.
- 25 to 30: Overweight.
- 30 to 40: Obesity.
- Over 40: Morbid Obesity.
"""
peso = float(input('Qual é o seu peso (Kg)?\t'))
altura = float(input('Qual é a sua altura (m)?\t'))
imc = peso / (altura ** 2)
print(f'O IMC é de {imc:.1f}.')
if imc < 15.5:
    print('ABAIXO DO PESO normal.')
elif 18.5 < imc < 25:
    print('PESO NORMAL.')
elif 25 < imc < 30:
    print('SOBREPESO.')
elif 30 < imc < 40:
    print('OBESIDADE.')
elif imc > 40: print('OBESIDADE MÓRBIDA.')