quant_idade = 5
cont = 0
soma_idades = 0
for cont in range(0,quant_idade,1):
    idades =int(input("insira a sua idade, depois, será calculada a média:"))
    soma_idades = soma_idades + idades
    cont = cont+1
print("a média das idades é de",(soma_idades/quant_idade))
