carros=[
    ["modelo", "HB20"],
    ["Fabricante", "Honda"],
    ["Ano", 2016]
]

carros[2][1]=2019

print(carros[1][1]+"\n")

for l,c in carros:
    print(l + " | "+ str(c))

print("--------------------------")

original =[[0,0,0],
           [0,0,0]]

transposta=[[0,0],
            [0,0],
            [0,0]]

for lin in range(0,2):
    for col in range(0,3):
        original[lin][col] = float(input("Número: "))

for lin in range(0,2):
    for col in range(0,3):
        transposta[col][lin]=original[lin][col]

print(original)
print(transposta)