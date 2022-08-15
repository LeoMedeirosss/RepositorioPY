matriz=[[],[],[]]

soma_impar = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f"digite o numero que será colocado na matriz [{linha}][{coluna}]: ")))

for linha in range(3):
    for coluna in range(3):

        if matriz[linha][coluna]%2 == 1:
            soma_impar+=matriz[linha][coluna]
            print(f"{soma_impar}")



    
