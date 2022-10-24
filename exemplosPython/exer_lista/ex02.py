from re import I
from statistics import median


meses = ["Janeiro", "Fevereiro", "Março","Abril", "Maio","Junho","Julho", "Agosto","Setembro","Outubro","Novembro","Dezembro"]
temperatura = []
acima_media = []

for i in range(len(meses)):
    temperatura.append(
        float(input("Informe a temperatura média do mês de " + meses[i] + ": ")))
print("Média Anual: ", median(temperatura))

for i in range(len(meses)):
    if (temperatura[i] > median(temperatura)):
        acima_media.append(temperatura[i])
        print("Média: ")
        print("Valores acima da Média: ")
        print("Mês de ", meses[i], "Valor => ", acima_media)
        print(f"Mês de {meses[i].upper()} temperatura { acima_media} ºC")
