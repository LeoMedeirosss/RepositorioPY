try:
    def HoraMinuto(Horas):
        Horas = Horas * 60
        print(Horas,"minutos")

    def HoraSegundo(Horas):
        Horas = Horas * 3600
        print(Horas,"segundos")

    Horas = int(input("digite aqui a quantidade Horas:"))
    Escolha = int(input(" para converter de hora pra minuto, digite 1.Para converter de hora pra segundo, digite 2:"))
    if Escolha == 1:
        HoraMinuto(Horas)
    elif Escolha == 2:
        HoraSegundo(Horas)
except ValueError:
    print("digite apenas números!")
