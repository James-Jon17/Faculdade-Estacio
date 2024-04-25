#casas precisas arredonda para cima
lista_numeros = [9.56783, 7.57568, 3.00914, 6.2321]

lista_precisao = [2, 2, 3, 3]

lista_nova = lambda numeros: [round(numero) for numero in numeros]

print(lista_nova(lista_numeros))

#pra cima e mais simplificado
lista_numeros2 = [8.56783, 6.57568, 2.00914, 5.2321]

lista_nova2 = list(map(round, lista_numeros2))

print(lista_nova2)


#conforme as casas precisas e simplificado
lista_numeros3 = [9.56783, 7.57568, 3.00914, 6.2321]
lista_precisao2 = [2, 2, 3, 3]

lista_nova3 = list(map(lambda x, p: round(x, p), lista_numeros3, lista_precisao2))

print(lista_nova3)

#solucao professor
lista_numeros4 = [9.56783, 7.57568, 3.00914, 6.2321]
lista_precisao3 = [2, 2, 3, 3]

arredondamento = lambda x,y: round(x,y)

resultado = list(map(arredondamento, lista_numeros4, lista_precisao3))

print(resultado)