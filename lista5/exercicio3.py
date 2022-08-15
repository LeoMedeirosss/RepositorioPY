numero_dna = int(input())

for n in range(numero_dna):
    arranjo = str(input())
    complemento = str(input())
if arranjo[0] == 'a' and complemento[0] == 't':
    print("COMPLEMENTARES")
elif arranjo[0] == 't' and complemento[0] == 'a':
    print("COMPLEMENTARES")
elif arranjo[0] == 'c' and complemento[0] == 'g':
     print("COMPLEMENTARES")
elif arranjo[0] == 'g' and complemento[0] == 'c':
    print("COMPLEMENTARES")
else:
    print("NAO COMPLEMENTARES")