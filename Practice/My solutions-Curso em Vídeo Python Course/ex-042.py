"""
NOME/NAME: Raphael Araújo
DATA/DATE: 31/10/2019
[PT]
> Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais.
- ISÓSCELES: dois lados iguais, um diferente.
- ESCALENO: todos os lados diferentes.
[EN]
> Redo CHALLENGE 035 of the triangles, adding the ability to show what type of triangle will be formed:
- BALANCER: all sides equal.
- ISOSCELES: two equal sides, one different.
- SCALENE: all different sides.
"""
reta1 = float(input('Primeiro segmento: \t'))
reta2 = float(input('Segundo segmento: \t'))
reta3 = float(input('Terceiro segmento: \t'))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO!')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima não podem formar um triângulo!')