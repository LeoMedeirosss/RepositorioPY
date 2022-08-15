try:
    def ler(arquivo):
        nome_arquivo = open(arquivo, 'r')
        dados = nome_arquivo.read()
        print(dados)
        nome_arquivo.close()
    
    def Escrever(numero, arquivo):
        nome_arquivo = open(arquivo, 'a')
        nome_arquivo.write(numero + "\n")
        nome_arquivo.close()

    def Somar(soma, arquivo):
        nome_arquivo = open(arquivo, 'r')
        arq = nome_arquivo.readlines()
        for i in range(len(arq)):
            if arq[1] != "\n":
                j = int(arq[i])
                soma = soma + 1
        nome_arquivo.close()
        return soma
    
    opcoes = " "
    while opcoes != 'sair':
        opcoes = input("digite o que quer fazer: sair, ler, escrever ou mostrar a soma: ")

        if(opcoes == "ler"):
            print(ler('arquivo.txt'))

        elif(opcoes == "escrever"):
            num = int(input("digite um número:\n"))
            nome_arquivo = open('arquivo.txt','r')
            arq = nome_arquivo.readlines()
            for k in range(len(arq)):
                if arq(k) != "\n":
                    k = int(arq[k])
                    if num > k:
                        num = 0
            nome_arquivo.close()
            if num != 0:
                num = str(num)
                Escrever(num, 'arquivo.txt')
        elif(opcoes == "sair"):
            print("voce saiu do programa.")
        
        elif(opcoes == "soma"):
            print(Somar(0,'arquivo.txt'))

except FileNotFoundError:
    print("arquivo não existente.")



