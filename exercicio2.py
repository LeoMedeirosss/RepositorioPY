funcionarios = int(input("escreva a quantidade de funcionários na empresa:"))
cont = 0
while cont<funcionarios:
    salario = float(input("agora, escreva o seu salário para vermos o seu aumento:"))
    cont = cont + 1
    if salario <= 3000:
        print("o seu salario passou de",salario,"para", salario * 1.1)
    elif salario > 3000 and salario < 5000:
        print("o seu salario passou de",salario,"para", salario * 1.2)
    elif salario > 5000 and salario < 7000:
        print("o seu salario passou de",salario,"para", salario * 1.3)
    else:
        print("o seu salario passou de",salario,"para", salario * 1.35)

    



