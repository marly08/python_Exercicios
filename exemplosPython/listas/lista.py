
lista_nomes =["marly", "aparecida", "gomes"]
print(len(lista_nomes))

lista_nomes.append("teste")
lista_nomes.insert(0,"primeiro nome")
for nome in lista_nomes:
    print(nome)


print("lsta completa ", lista_nomes )
print("quantidde de itens: ", len(lista_nomes))
print("  num : -> \n", lista_nomes[::-1])
print("  num : -> \n", lista_nomes[:-1])
print("0: 2-> \n",lista_nomes[::2])

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)
for frutas in fruits :
    print(frutas)
