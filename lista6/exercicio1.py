Q = int(input())
acumulador = 0
for i in range(Q):
    T,V = input().split()
    T,V = [int(T),int(V)]
    acumulador = (T*V) + acumulador
print(acumulador)

