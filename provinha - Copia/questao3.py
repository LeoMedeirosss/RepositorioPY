sexo = str(input("qual seu sexo? masculino ou feminino?"))
altura = float(input("qual a sua altura?"))
peso = float(input("qual o seu peso?"))

calculo_h = (72.7 * altura) - 58
calculo_m = (62.1 * altura) - 44.7

if sexo == "masculino":
    if calculo_h > peso:
        print("você está abaixo do peso")
    elif calculo_h == peso:
        print("você está no peso ideal")
    else:
        print("você está acima do peso")

if sexo == "feminino":
    if calculo_m > peso:
        print("você está abaixo do peso")
    elif calculo_m == peso:
        print("você está no peso ideal")
    else:
        print("você está acima do peso")
