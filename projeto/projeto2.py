import csv

#FAZER OS IMPORTS

def login():

    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    dadosUsuario = [login,senha]

    validarDadosLogin("dados.csv", dadosUsuario)

def printMenu():
    print("\tMenu de Funcionalidades")
    print("1. Assistente Virtual")
    print("2. Emociometro")
    print("3. Sair")

def anotar(arquivo, lista) :  #checar se o nome usuario já existe, se sim não anotar no csv
    with open(arquivo,'a') as arq:
        data = ','.join(lista)
        arq.writelines(data+'\n')

def JaExisteLogin(arquivo, login):
    with open(arquivo, "r") as arq:
        leitor = csv.reader(arq, delimiter="\n")
        usuarioExiste = False;
        for line in leitor:
            loginsExistentes = line[0].split(',')[0]
            if (loginsExistentes == login):
                usuarioExiste = True;
        return usuarioExiste

def validarDadosLogin(arquivo,dados):
    with open(arquivo, "r") as arq:
        leitor = csv.reader(arq, delimiter="\n")
        usuarioExiste = False;
        senhaCorreta = False;
        for line in leitor:
            loginUsuario = line[0].split(',')[0]
            senhaUsuario = line[0].split(',')[1]
            
            if (loginUsuario == dados[0]):
                usuarioExiste = True;
        if (senhaUsuario == dados[1]):
            senhaCorreta = True
        if (usuarioExiste and senhaCorreta):
            print("Usuário encontrado!")
            printMenu()
        elif(usuarioExiste and not(senhaCorreta)):
            print("Senha incorreta! tente novamente")
            login()
        else:
            print("usuário não existe! Faça o cadastro")
            cadastroAluno()
                            

def assistenteVirtual():
    print("ASSISTENTE VIRTUAL")

def cadastroAluno():

    nome = input("Digite o seu nome completo: ")
    idade = int(input("Digite a sua idade: "))
    login = input("Digite o seu login: ").lower()
    while (JaExisteLogin("dados.csv",login)):
        print("Esse login ja existe. Tente outro!")
        login = input("Digite o seu login: ").lower()
    senha = input("Digite a sua senha: ")
    confSenha = input("Confirme a sua senha: ")

    while (senha != confSenha):
        confSenha = input("Confirme a sua senha: ")

    dadosCadastro = [login, senha]

    anotar("dados.csv", dadosCadastro)

def emociometro():    
    print("EMOCIOMETRO")


botaoCadastroLogin = int(input("Cadastro-1, Login-2: "))
x = True

while (x):
    if (botaoCadastroLogin == 1):
        cadastroAluno()
        login()
        x = False
    elif(botaoCadastroLogin == 2):
        login()
        x = False
    else:
        print("Erro. Digite 1 ou 2")
        botaoCadastroLogin = int(input("Cadastro-1, Login-2: "))      

botaoAssitenteEmociometro = int(input("Assitente Virtual-1, Emociometro-2, 3-Sair"))
y = True
while (y):
    if (botaoAssitenteEmociometro == 1):
        assistenteVirtual()
        y = False
    elif(botaoAssitenteEmociometro == 2):
        emociometro()
        y = False
    elif(botaoAssitenteEmociometro == 3):
        y = False    
    else:
        print("Erro. Digite 1, 2 ou 3")
        botaoAssitenteEmociometro = int(input("Assitente Virtual-1, Emociometro-2, 3-Sair: "))