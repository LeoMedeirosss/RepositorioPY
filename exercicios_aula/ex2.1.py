matriz=[[],[],[]]

soma_coluna = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f"digite o numero que será colocado na matriz [{linha}][{coluna}]: ")))

    
for linha in range(3):
    soma_coluna+=matriz[1][0]
    print(f"{soma_coluna}")
