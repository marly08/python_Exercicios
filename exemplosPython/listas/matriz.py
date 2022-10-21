# matriz com 3 linhas e 3 colunas
matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


# usuario decide quantas colunas e quantas linhas
matriz = []
T = int(input("Digite o número de colunas:"))
U = int(input("Digite o número de linhas:"))
for i in range(T):
    matriz.append([])

for l in range(0, T):
    for c in range(0, U):
        matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))

for l in range(0, T):
    for c in range(0, U):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
