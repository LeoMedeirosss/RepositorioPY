vetor = []
cont = 0

for v in range(3):
    vetor.append(int(input("digite aqui 3 numeros por favor: ")))

print("o maior número do vetor é:{0}".format(max(vetor)))
print()
print("o maior número(em binario) é {0:b}".format((max(vetor))))
print()
for v in range(3):
    if vetor[v] > 5:
        cont = cont+1
print("a quantidade de numeros maiores que 5 é:",cont)
média = (vetor[0]+vetor[1]+vetor[2])/3
print("a média dos números do vetor é:",média)
print("o menor número(em octa) é {0:o}".format((min(vetor))))