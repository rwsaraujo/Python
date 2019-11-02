"""
NOME/NAME: Raphael Araújo
DATA/DATE: 01/11/2019
[PT]
> Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
[EN]
> Create Python code that tests if the pudding site is accessible from the computer you use.
"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acssível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())
