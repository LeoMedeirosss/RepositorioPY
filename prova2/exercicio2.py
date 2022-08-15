dicionario = {}

for i in range(3):
    nomeG = input("digite o nome do grupo:")
    m1 = float(input("digite a altura do primeiro membro:"))
    m2 = float(input("digite a altura do segundo membro:"))
    m3 = float(input("digite a altura do terceiro membro:"))
    total = (m1+m2+m3)/3

    dicionario[nomeG]=total

print(dicionario)
print("o grupo que tem a maior média de altura é o grupo",max(dicionario, key =dicionario.get).title())
