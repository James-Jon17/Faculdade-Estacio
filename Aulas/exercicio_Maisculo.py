veiculos = ['aviao', 'carro', 'navio', 'onibus']

veiculos_maisculo = list(map(str.upper, veiculos))

print(veiculos)
print(veiculos_maisculo)

f_maiscula = lambda x: str.upper(x)


veiculos_maisculo2 = list(map(f_maiscula, veiculos))
veiculos_maisculo2.append("Jato".upper())

print(veiculos_maisculo2)