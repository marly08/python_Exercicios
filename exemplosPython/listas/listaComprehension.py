#dobrar o valor de um dado
#todos os valores acima de U$$1000, imposto  de 50% sobre o valor

lista_precos = [500, 1500, 2000, 100, 25]
#caso1(normal)
nova_lista=[]
for preco in lista_precos:
    nova_lista.append(preco*2)
print("lista1->",nova_lista)

#caso2
imposto=[]
for imp in lista_precos:
    if imp >= 1000:
        imposto.append(imp*0.5)
print("imposto1-> ", imposto)

#comprehesion
#caso1
nova_lista2 = [preco *2 for preco in lista_precos]
print("lista2->",nova_lista2)
#caso2
imposto2=[imp2 * 0.5 for imp2 in lista_precos if imp2 >= 1000]
print("imposto2-> ",imposto2)


