matriz = [ [], [], [] ]
vetor_soma = []


for i in range (3):
    for l in range(3):
        matriz[i].append(float(input("insira aqui os números da matríz:")))

for i in range(3):
    for l in range(3):
        print(f"[{matriz[i][l]:^4}]", end=" ")
    print()

soma_coluna1 = matriz[0][0] + matriz[1][0] + matriz[2][0]
soma_coluna2 = matriz[0][1] + matriz[1][1] + matriz[2][1]
soma_coluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]

vetor_soma = soma_coluna1, soma_coluna2, soma_coluna3

print(vetor_soma)
