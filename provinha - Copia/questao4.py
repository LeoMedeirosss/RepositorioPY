matriz_trab = [[],[],[]]
soma_salario = 0
cont = 0

for l in range(3):
    for c in range(3):
        matriz_trab[l].append(int(input(f"Profissão {l + 1}, escreva o seu salário médio, tempo mínimo para trabalho e o quanto ganha por hora:")))

for l in range(3):
    for c in range(3):
        print(f"[{matriz_trab[l][c]:^4}]", end=" ")
    print()

for l in range(3):
    soma_salario += matriz_trab[l][0]
media_salario = soma_salario / 3

print(f"A média salarial das 3 profissões é: {media_salario}.")

soma_diag = matriz_trab[0][0] + matriz_trab[1][1] + matriz_trab[2][2]

print(f"A soma dos valores da diagonal principal da matriz é: {soma_diag}.")