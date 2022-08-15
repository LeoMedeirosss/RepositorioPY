try:
    contMaior = 0
    contMenor = 0
    contIgual = 0
    numeros = []
    
    for n in range(10):
        
        numeros1 = int(input("digite um número:"))
        numeros.append(numeros1)
        
        for c in range(10):
            
            if numeros[n] > numeros[0]:
                contMaior = contMaior + 1
            elif numeros[n] == numeros[0]:
                contIgual = contIgual + 1
            elif numeros[n] < numeros[0]:
                contMenor = contMenor + 1
    print("a quantidade de números maiores que o primeiro é de",(contMaior/10),"números")
    print("a quantidade de números menores que o primeiro é de",(contMenor/10),"números")
    print("a quantidade de números iguais ao primeiro é de",(contIgual/10) - 1,"números")

except ValueError:
    print("por favor, digite apenas números inteiros.")

    