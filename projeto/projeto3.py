import csv

def printMenu():
    print("\tMenu de Funcionalidades")
    print("1. Assistente Virtual")
    print("2. Emociometro")
    print("3. Sair")

def login():

    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    dadosUsuario = [login,senha]

    validarDadosLogin("dados.csv", dadosUsuario)

def anotarDadosCadastro(arquivo, lista) :  #checar se o nome usuario já existe, se sim não anotar no csv
    with open(arquivo,'a') as arq:
        data = ','.join(lista)
        arq.writelines(data)

def anotarDadosFeedbackAssistenteVirtual(arquivo, lista) : 
    with open(arquivo,'a') as arq:
        data = ','.join(lista)
        arq.writelines(','+data+',')

def anotarDadosFeedbackEmociometro(arquivo, lista) : 
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
                            

def cadastroAluno():

    nome = input("Digite o seu nome completo: ")
    matricula = input("Digite a sua matricula (modelo XXXXXX): ")
    while (len(matricula) != 6):
        matricula = input("Digite a sua matricula (modelo XXXXXX): ")
    login = matricula    
    while (JaExisteLogin("dados.csv",login)):
        print("Esse login ja existe. Tente outro!")
        login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")
    confSenha = input("Confirme a sua senha: ")

    while (senha != confSenha):
        confSenha = input("Confirme a sua senha: ")

    print("Parabéns! Seu cadastro foi realizado com sucesso, seja muito bem-vindo.")

    dadosCadastro = [login, senha, nome]

    anotarDadosCadastro("dados.csv", dadosCadastro)

def emociometro():
    resp = input("O Emociômetro está disponível! Que tal responder agora e ficar livre disso? [S] ou [N]").lower()
    if resp == 's':
        print("O Emociômetro é uma escala de humor. Preencha (numa escala de 0 a 10) como você está se sentindo e e assim saberemos como te ajudar.")

        print("o colegio será responsavel pelas perguntas que irá fazer no emociometro:")

        pergunta1 = input("Primeira pergunta: O que você achou em relação a aula de campo? ")
        pergunta2 = input("Segunda pergunta: O que você achou em relação a semana de provas? ")
        pergunta3 = input("Terceira pergunta: O que você achou em relação as aulas práticas da semana? ")

        notasPerguntas = [pergunta1,pergunta2,pergunta3]
        anotarDadosFeedbackEmociometro("dados.csv", notasPerguntas)

def assistenteVirtual():
    print("ASSISTENTE VIRTUAL")
    resp = input("Olá, como posso te ajudar? \nA) Quero falar com a Escola\nB) Quero pedir ajuda\n").lower()
    #adiciona no arquivo Escola ou pedir ajuda
    if resp == 'a':
        resp1 = input("Com qual setor você quer falar?\nA) Coordenação ou Gestão\nB) Psicopedagógico\n")
        #adiciona no arquivo qual setor
        resp2 = input("Sobre o que você quer falar com essse setor?\nA) Assunto pessoal\nB) Relatar um acontecimentos\nC) Sobre minha situação quanto aluno\nD) Sugestões\n")
        #adiciona no arquivo a escolha
        print("Obrigado, a escola foi informada!")
    else:
        resp1 = input("Com o que você precisa de ajuda? \nA) Provas\nB)Notas\nC)Datas e Anuncios")
        #adiciona no arquivo a escolha, essa parte a gnt deixa so isso pq se for pra aprofundar n tem oq botar
        resp2 = input("Deseja buscar ajuda da coordenação ou secretaria? \nA)Coordenação\nB)Secretaria")
    respostas = [resp1, resp2]
    anotarDadosFeedbackAssistenteVirtual("dados.csv", respostas)

print("Olá, Estudante! Sou Mafalda a sua assitente virtual.\nMinha funcao é ajudar voce a se comunicar e expressar seus sentimentos sem medo.")

botaoCadastroLogin = int(input("Para fazer o Cadastro digite 1, para o Login 2: "))
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

botaoAssitenteEmociometro = int(input("Assitente Virtual-1, Emociometro-2, 3-Sair: "))
y = True
while (y):
    if (botaoAssitenteEmociometro == 1):
        assistenteVirtual()
        botaoAssitenteEmociometro = int(input("Assitente Virtual-1, Emociometro-2, 3-Sair: "))
        if (botaoAssitenteEmociometro == 3):
            y = False
    elif(botaoAssitenteEmociometro == 2):
        emociometro()
        y = False
    elif(botaoAssitenteEmociometro == 3):
        y = False    
    else:
        print("Erro. Digite 1, 2 ou 3")
        botaoAssitenteEmociometro = int(input("Assitente Virtual-1, Emociometro-2, 3-Sair: "))