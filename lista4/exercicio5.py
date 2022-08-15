matriz = [[], [], []]


for e in range(3):
    for s in range(3):
        matriz[e].append(float(input(f"Estagiário de CC {1 + e},escreva o seu salário, em seguida o vale transporte e o vale alimentação:")))

soma_vale_transporte = matriz[0][1] + matriz[1][1] + matriz[2][1]
media_salário = (matriz[0][0] + matriz[1][0] + matriz[2][0])/3

print("a soma do valor do vale-transporte dos estagiários é de",soma_vale_transporte)
print("a média salarial entre os 3 estagiários de Ciência da Computação é de",media_salário)

