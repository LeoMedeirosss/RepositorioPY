vetorA = []
vetorB = []
vetorC = []


for i in range(10):
    vetor = int(input("digite os valores do vetor:"))
    vetorA.append(vetor)
    if(vetor % 2 == 1):
        vetorB.append(vetor)
    else:
        vetorC.append(vetor)

print("Todos os números colocados dentro do vetor são:")
print(vetorA)
print(f"os números ímpares colocados dentro do vetor são:")
print(vetorB)
print(f"osnúmeor páres colocados dentro do vetor são:")
print(vetorC)
    
