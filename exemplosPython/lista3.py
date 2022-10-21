from ctypes.wintypes import PINT


lista_lojas = ["Pirapora", "Buritizeiro", "Varzea da Palma" ]
lista_faturamento = [200, 600, 350]


#remover= del_remove_pop
#vincular listas
resultados =[]
for i in range(3):
    tupla = (lista_lojas[i-1], lista_faturamento[i-1])
    resultados.append(tupla)
    
print(resultados)
print("faturamento loja Pirapora: ", resultados[1][1])



profissao = ["medico", "professor", "cozinheira", "ator", "ator"]
salario = [222, 332, 334, 777]


salario.sort()
print(salario)

profissao.sort()
for i in profissao:
    print(i)

profissao.sort(reverse=True)
for i, j in enumerate(profissao):
    print(i+1, '->', j)

profissao.extend(["mergulhador", "marinheiro"])
print(profissao)
x = profissao.count("ator")
print(x)
print(profissao.index("mergulhador"))

texto = "www.marlly.hotmail.com".split(".")
texto = "marlly email hotmail.com".split(" ")
print(texto)
