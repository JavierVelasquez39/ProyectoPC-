import random

m = int(input("Ingrese el número de filas (m): "))
n = int(input("Ingrese el número de columnas (n): "))

matriz = [[random.randint(-20, 20) for _ in range(n)] for _ in range(m)]
print("Matriz original:")
for fila in matriz:
    print(fila)

matriz_traspuesta = [[matriz[j][i] for j in range(m)] for i in range(n)]
print("Matriz traspuesta:")
for fila in matriz_traspuesta:
    print(fila)