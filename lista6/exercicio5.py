def tabuada (multi, cont):
    resp = multi*cont
    return(resp)

multiplicador = int(input())
resp = 0

contador = -1
num = contador
while num <10:
    num = num + 1
    resp = tabuada(multiplicador,num)
    print('{} x {} = {}'.format(num, multiplicador, resp))