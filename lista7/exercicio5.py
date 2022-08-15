import random
numeros = []
def sorteia():
    for n in range(10):
        numeros1 = random.randint(0,200)
        numeros.append(numeros1)
    print(numeros)
def operacao():
    impares = 0
    pares = 0
    for i in range(10):
        if numeros[i] % 2 == 1:
            impares = impares + numeros[i]
        elif numeros[i] % 2 == 0:
            pares = pares - numeros[i]
    print("a soma de todos os impares é de:",impares)
    print("a subtração de todos os pares é de:",pares)
sorteia()
operacao()


