def escrever(nome_arquivo):
    nome = []
    sobrenome = []
    idade = []
    arquivo=open(nome_arquivo,"w")
    quantidade = int(input("digite a quantidade de pessoas:"))
    for n in range(quantidade):
        nome1 = input("digite o nome:")
        nome.append(nome1)
        sobrenome1 = input("digite o sobrenome:")
        sobrenome.append(sobrenome1)
        idade1 = input("digite a idade:")
        idade.append(idade1)
        arquivo.write("Nome:"+ nome[n])
        arquivo.write(" "+ sobrenome[n])
        arquivo.write(" Idade:" + idade[n])
        arquivo.write("\n")
    arquivo.close
def ler(nome_arquivo):
    arquivo = open(nome_arquivo,"r")
    print(arquivo.read())
nome_arquivo = input("digite o nome do arquivo:")
escrever(nome_arquivo)
ler(nome_arquivo)


