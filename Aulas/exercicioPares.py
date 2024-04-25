lista = [0,1,1,2,3,5,8,13,21,34]

pares = lambda x: x % 2 == 0

numeros_pares = filter(pares, lista)
print(list(numeros_pares))
print("teste de paridade:", pares(5))

lista.append(36)
numeros_pares2 = list(filter(pares, lista))
print(numeros_pares2)
print("teste de paridade:", 5 in lista)