def escrever(nome_arquivo):
   try:
       nome=[]
       idade=[]
       arquivo=open(nome_arquivo,"w")
       nome1=input("Digite um nome:")
       nome.append(nome1)
       while nome1!="Sair":
           idade1=input("Digite uma idade:")
           idade.append(idade1)
           nome1=input("Digite um nome:")
           nome.append(nome1)
       arquivo.write("\n".join(nome))
       arquivo.write("\n".join(idade))
       arquivo.close()
   except TypeError:
       print("Sóéaceitootipo string!")
   except ValueError:
       print("Digiteaidade usando valores numéricos!")
def ler(nome_arquivo):
    try:
        arquivo=open(nome_arquivo,"r")
        print(arquivo.read())
    except FileNotFoundError:
        print("Arquivo não existe!")
nome_arquivo=input("Digiteonome do arquivo:")
escrever(nome_arquivo)
ler(nome_arquivo)