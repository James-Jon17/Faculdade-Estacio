"""Tentei criar o mesmo resultado do professor,
porém a regra foi implementada de forma diferente,
e obtive outra respota"""
numeros = [1,2,3,4,5,6,7,8,9,10]

lista_completa_somada = list(map(lambda x: x + x, numeros))
lista_somada = sum(map(lambda x: x + x, numeros))

print(lista_completa_somada)
print(lista_somada)

#solucao professor
from functools import reduce

f_soma = lambda x,y: x + y

numeros2 = [1,2,3,4,5,6,7,8,9,10]

resultado = reduce(f_soma, numeros2)
print(resultado)