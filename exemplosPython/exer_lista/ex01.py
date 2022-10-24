# mostrar lista com numeros e sua posição
inteiros = [4, 5, 3, 6, 8]
for i, num in enumerate(inteiros):
    print("indice ", i, "=>", num)

print("Ordem Reversa: ", inteiros[::-1])  # lista em ordem inversa

media = (sum(inteiros)) / (len(inteiros))  # media da lista
print("Média da lista: ", media)

print("Maior Número", max(inteiros))  # maior número
print("Menor Número", min(inteiros))  # menor número

pares = []
impares = []

for i in inteiros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print("Lista PAR: ", pares)
print("Lista Impar: ", impares)
