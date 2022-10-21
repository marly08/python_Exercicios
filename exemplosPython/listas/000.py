from tkinter import INSERT


numeros = [2, 5, 3, 8, 13, 22]
numeros.append(0)
numeros.insert(1, 1)
numeros.extend([55,76])

for i, j in enumerate(numeros):
    print(i, "->", j)


numeros.sort()
for i in numeros:
    print(i)

print(len(numeros))

numeros.sort(reverse=True)
print(numeros)

x = numeros.count(8)
print("tamanho = COUNT", x)

x = range(3, 6)
for n in x:
    print(n)
a = sum(x)
print("soma: ", a)

tababuada = range(1, 11)
for i, t in enumerate(tababuada):
    print(i, " x ", t, "= ", i*t)
