fruta = ["banana", "maca", "morango"]
cor = ["amarelo", "vermelho", "morango"]

frutaCor = []
for i in range(len(fruta)):
    tupla = (fruta[i], cor[i])
    frutaCor.append(tupla)
print(frutaCor)
for i in frutaCor:
    print(i)
