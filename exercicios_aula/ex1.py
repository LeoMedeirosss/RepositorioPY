matriz=[[],[],[],[]]
for linha in range(4):
    for coluna in range(4):
        matriz[linha].append(int(input(f"digite o numero que será colocado na matriz [{linha}][{coluna}]: ")))

for linha in range(4):
    for coluna in range(4):
        print(f"[{matriz[linha][coluna]:4^}]", end="")
    print()

print(matriz)