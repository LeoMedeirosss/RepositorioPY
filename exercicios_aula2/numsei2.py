try:
    arq = open("arquivo.txt")
    linha = arq.readline()
    arq.close
except FileNotFoundError:
    print("arquivo não encontrado!")