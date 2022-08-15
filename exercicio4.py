reta1 = float(input("insira o comprimento da primeira reta do seu triângulo:"))
reta2 = float(input("insira o comprimento da segunda reta do seu triângulo:"))
reta3 = float(input("insira o comprimento da terceira reta do seu triângulo:"))

if reta1 + reta2 < reta3:
    print("seu triângulo não existe")
elif reta2 + reta3 < reta1:
    print("seu triângulo não existe")
elif reta3 + reta1 < reta2:
    print("seu triângulo não existe")
else:
    print("seu triângulo existe")