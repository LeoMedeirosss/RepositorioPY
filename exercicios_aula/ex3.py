matriz = [ [], [] ,[] ]
soma_turma = 0
for aluno in range(3):
    for nota in range(4):
        matriz[aluno].append(int(input(f"Digite a nota{nota} para o aluno{aluno}:")))
        soma_turma+=matriz[aluno][nota]
print(f"a média das notas dos alunos é igual a",soma_turma/12)
