from xmlrpc.server import list_public_methods


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("Números de 1 até 9: ", lista_numeros[:9])  # 1 ate 9
print("Números de 8 até 13: ", lista_numeros[7:13]) #8 ate 13

pares = []
impares = []
for num in lista_numeros: # numeros pares
    if num % 2 == 0:
        pares.append(num) 
    else :
        impares.append(num)  

print("lista de números Pares : ", pares)
print("lista de números Impares : ", impares)


print("List Reversa: ", lista_numeros [::-1]) #list reversa

