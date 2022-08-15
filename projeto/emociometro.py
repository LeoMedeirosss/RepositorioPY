arquivo_emociometro = open("emociometro.txt", "a")
mtfeliz = 0
feliz = 0
neutro = 0
triste = 0
mttriste = 0

print("o colegio será responsavel pelas perguntas que irá fazer no emociometro:")
print("Qual a sua emoção em relação á ______________")
try:
    qnt_perguntas = int(input("insira aqui quantas perguntas serão feitas pelo colégio:"))
    for n in range(qnt_perguntas):
        emocao = int(input(" carinha muito feliz(5)\n carinha feliz(4)\n carinha neutra(3)\n carinha triste(2)\n carinha muito triste(1)\n"))
        if emocao == 5:
            mtfeliz = mtfeliz + 1
            arquivo_emociometro.write("mtfeliz")
        elif emocao == 4:
            feliz = feliz + 1
            arquivo_emociometro.write("feliz\n")
        elif emocao == 3:
            neutro = neutro +1
            arquivo_emociometro.write("neutro\n")
        elif emocao == 2:
            triste = triste + 1
            arquivo_emociometro.write("triste\n")
        elif emocao == 1:
            mttriste = mttriste + 1
            arquivo_emociometro.write("mttriste\n")
except:
    print("por favor, digite numeros entre 5(mais contente) e 1(mais descontente)")