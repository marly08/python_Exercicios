from ctypes.wintypes import PINT


lista_lojas = ["Pirapora", "Buritizeiro", "Varzea da Palma" ]
lista_faturamento = [200, 600, 350]
lista_faturamento.sort()
print(lista_faturamento)
lista_faturamento.sort(reverse=True)
print(lista_faturamento)
#vincular listas
resultados =[]
for i in range(3):
    tupla = (lista_lojas[i-1], lista_faturamento[i-1])
    resultados.append(tupla)
    
print(resultados)
print("faturamento loja Pirapora: ", resultados[1][1])