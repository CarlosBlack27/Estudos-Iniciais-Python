'''
Verifica se a base da URL esta de acordo com o padrão correto

Exemplos de URLs validas:
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio

Exemplos de URLs inválidas:
    https://bytebank/cambio
    https://bytebank.naoexiste/cambio
    ht://bytebank.naoexiste/cambio
'''
#https://www.bytebank.com.br/cambio
import re

url = 'www.bytebank.com.br/cambio'
padrao_URL = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_URL.match(url)

if  not match:
    raise ValueError("A URL não é válida")

print("A URL é válida ")
