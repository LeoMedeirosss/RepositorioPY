tabela_preco = [[1,2,3,4] , [5.3,6,3.2,2.5]]
valor_final = 0
descontinho = 0

codigo = int(input())

quantia = int(input())

for c in range(4):
    if codigo == tabela_preco[0][c]:
        valor_final = (quantia * tabela_preco[1][c])
    if quantia >= 15 or valor_final >= 40:
        descontinho = valor_final * 0.15


valor_final = valor_final - descontinho
print("R$ ",valor_final)
        




