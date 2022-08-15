aluno = input('Digite o nome ou número do aluno: ')
fclasse = open('classe.txt', 'r')
id_aluno = -1

for linha in fclasse:
    linha = linha.split()
    if linha[0] == aluno or linha[1] == aluno:
        id_aluno = linha[0]
        break
fclasse.close()

if id_aluno == -1:
    print("Aluno inexistente!")
else:
    fnotas = open('notas.txt', 'r')
    for linha in fnotas:
        linha_str = linha.split()
    if linha_str[0] == id_aluno:
        print(linha)
    fnotas.close()
