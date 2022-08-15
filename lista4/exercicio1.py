vetor = []

for f in range(10):
    farenheit = float(input("digite aqui uma temperatura em Farenheit:"))
    vetor.append(farenheit)

for i in range(10):
    vetor[i] = (vetor[i] - 32) * (5/9)

print("as temperaturas em Celsius são:")

for i in vetor:
    print(i)




