matriz = [ [], [] ,[],[] ]
soma_turma = 0
for trimestre in range(4):
    for regioes in range(5):
        matriz[trimestre].append(int(input(f"No trimestre{trimestre+1}, digite a quantidade vendida na região{regioes+1}:")))
        soma_turma+=matriz[trimestre][regioes]
print(f"a quantidade total vendida é de",{soma_turma})