nome = ["primiro", 2, 4, 5, "Marly", "Aparecida", "gomes", "ultmimo"]
print("indice 3 ", nome[3])
print("indice -3 ", nome[-3])
print("indice 3: ", nome[3:])
print("indice :3 ", nome[:3])
print("indice [:] ", nome[:])
print("indice :3-3 ", nome[:-3])
print("indice ::1 ", nome[::1])
print("indice ::-1 ", nome[::-1])

for indice in nome:
    print(indice)

lista_numeros = [2, 5, 45, 3, 7, 8, 90]
for indice in lista_numeros:
    print(indice)

print(" Numero de elemntos da lista: " + str(len(lista_numeros)))
lista_numeros.append(100)
lista_numeros.insert(0, 0)
lista_numeros.sort()
print("lista ordenada com SORT() ", lista_numeros)
lista_numeros.pop(2)
del lista_numeros[5]
lista_numeros.sort()
print("lista ordenada com SORT()  indice 2 apagadoPOP(2) REMOVE del lista_numeros(5): " + str(lista_numeros))
