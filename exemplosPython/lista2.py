lista_compras = ["maça", "banana", "limão", "laranja", "Carro"]
print(lista_compras)

lista_sonhos = []
print(lista_sonhos)

sonho = lista_compras.pop(-1)
print(sonho)

lista_sonhos.append(sonho)
print(lista_sonhos)

tarefas = []
tarefa = "vazio"
while tarefa != '':
    tarefa = input("Insira uma tarefa: ")
    tarefas.append(tarefa)

print(tarefas)
print("sem a ultima casa vazia: [0:-1] ", tarefas[0:-1])
