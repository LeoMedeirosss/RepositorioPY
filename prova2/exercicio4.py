import random
N = int(input('Digite um inteiro:'))
fsaida = open('saida.txt', 'w')
fnomes = open('nomes.txt', 'r')
  
cont = 0
for nome in fnomes:
    cont = cont + 1
nnomes = cont

fnomes.close()

for i in range(0,N):
    fnomes = open('nomes.txt', 'r')
    fsobrenomes = open('sobrenomes.txt', 'r')
    id_nome = random.randint(1, nnomes)
    id_sobrenome = random.randint(1, nnomes)

    nome = ""
    sobrenome = ""
  
    cont = 1
    for linha in fnomes:
        if cont == id_nome:
            nome = linha # salva nome
            break
        cont = cont + 1
    cont = 1
    for linha in fsobrenomes:
        if cont == id_sobrenome:
            sobrenome = linha
            break
        cont = cont + 1
    saida_str = nome.strip() + " " + sobrenome.strip()
    fsaida.write(saida_str)
    fsaida.write("\n")
  
    fnomes.close()
    fsobrenomes.close()
    