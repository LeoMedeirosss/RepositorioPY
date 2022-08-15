
vetorA=[]
vetorB=[]
soma_par = 0
soma_impar = 0
cont_impar = 0

for i in range(5):
    vetorA.append(float(input("digite aqui 5 números para o vetorA:")))
    
    
for i in range(5):
    vetorB.append(float(input("digite aqui 5 números para o vetorB:")))

vetorC = vetorA + vetorB


for i in range(10):
    if vetorC[i] % 2 == 0:
        soma_par = soma_par + vetorC[i]
    elif vetorC[i] % 2 == 1:
        soma_impar = soma_impar + vetorC[i]
        cont_impar = cont_impar + 1


print("o vetor C é",vetorC)
print("a média dos números ímpares é:",soma_impar/cont_impar)
print("a soma dos números pares é:",soma_par)
print("o menor número do vetor C é:",min(vetorC))


    

