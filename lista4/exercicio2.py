vetor_principal = []
cont_maior = 0
cont_menor = 0
cont_igual = 0

for i in range(10):
    vetor = int(input("digite aqui 10 números inteiros:"))
    vetor_principal.append(vetor)

for i in range(1,10):
    if vetor_principal[0] < vetor_principal[i]:
        cont_maior = cont_maior + 1
    elif vetor_principal[0] > vetor_principal[i]:
        cont_menor = cont_menor + 1
    else:
        cont_igual = cont_igual + 1

print(vetor_principal[0],"é o primeiro número digitado")
print(cont_maior,"números são maiores que o primeiro número digitado")
print(cont_menor,"números são menores que o primeiro número digitado")
print(cont_igual,"números são iguais que o primeiro número digitado")

