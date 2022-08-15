media = float(input())
faltas = int(input())

def ClassificaAluno():
    if media >= 9.5 and faltas <= 10:
        print("APROVADO COM LOUVOR")
    elif media >= 7.0 and faltas <= 10:
        print("APROVADO")
    elif media <= 6.9 and faltas <= 10:
        print("REPROVADO")
    elif faltas > 10:
        print("REPROVADO POR FALTAS")

ClassificaAluno()