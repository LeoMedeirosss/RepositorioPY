numero = int(input("insira um número, e depois veremos se ele é ou não primo:"))
cont = 0

for x in range(2,numero):
    if numero % x == 0:
        cont = cont + 1
        break
if cont == 0:
    print("esse número é primo")
else:
    print("esse número não é primo")


