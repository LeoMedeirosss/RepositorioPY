cont = 0
pergunta1 = int(input("Aconteceu um roubo, você conhece a vitima? (escreva 1 para 'sim' ou 2 para 'nao':"))
pergunta2 = int(input("Você esteve no local do roubo?"))
pergunta3 = int(input("Você mora perto da vítima?"))
pergunta4 = int(input("A vítima lhe devia dinheiro?"))
pergunta5 = int(input("Você já trabalhou com a vítima?"))

if pergunta1 == 1:
    cont+=1

if pergunta2 == 1:
    cont+=1

if pergunta3 == 1:
    cont+=1

if pergunta4 == 1:
    cont+=1
        
if pergunta5 == 1:
    cont+=1
    
if cont == 2:
    print("você é suspeito")
elif cont == 5:
    print("você é o ladrão")
elif cont == 3:
    print("você é cumplice")
elif cont == 4:
    print("você é cumplice")
else:
    print("você é inocente")
