matriz = []
colunas = int(input("Digite o número de colunas:"))
linhas = int(input("Digite o número de linhas:"))

for i in range(colunas):
    matriz.append([i])

for c in range(0,colunas):
    for l in range(0,linhas):
        matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
    
for c in range(0,colunas):
        for l in range(0,linhas):
              print(f'[{matriz[c][l]:^5}]', end='')
        print()