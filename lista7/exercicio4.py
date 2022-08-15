try:
  nome_arquivo = input("digite o nome do arquivo:")  
  arquivo = open(nome_arquivo,"r")
  dados = arquivo.read()
  linhas = arquivo.readlines()
  palavras = dados.split('\n')
  for linha in palavras:
    cont = 0
    for char in linha:
      if char == ' ':
        cont = cont + 1
    if cont > 5:
      print(linha)
  arquivo.close()
except FileNotFoundError:
    print("Esse arquivo não existe!")
