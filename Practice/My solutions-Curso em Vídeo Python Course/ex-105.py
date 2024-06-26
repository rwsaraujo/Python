"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com
as seguintes informações:
- Quantidade de notas.
- A maior nota.
- A menor nota.
- A média da turma.
- A situação (opcional).
Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
[EN]
> Make a program that has a grades function () that can receive multiple grades from students and will return a
dictionary with the following information:
- Number of notes.
- The highest grade.
- The lowest grade.
- The class average.
- The situation (optional).
Also add the docstrings of this function for query by the developer.
"""
def notas(*n, sit=False):
  """
  -> Função para analisar notas e situações de vários alunos.
  :param n: uma ou mais notas dos alunos (aceita várias).
  :param sit: valor opcional, indicando se deve ou não adicionar a situação.
  :return: dicionário com várias informações sobre a situação da turma.
  """
  r = dict()
  r['total'] = len(n)
  r['maior'] = max(n)
  r['menor'] = min(n)
  r['média'] = sum(n)/len(n)
  if sit:
    if r['média'] >= 7:
      r['situação'] = 'BOA'
    elif r['média'] >= 5:
      r['situação'] = 'RAZOÁVEL'
    else:
      r['situação'] = 'RUIM'
  return r


#Programa principal
resp = notas(5.5, 2.5, 1.5, sit=False)
print(resp)
help(notas)
