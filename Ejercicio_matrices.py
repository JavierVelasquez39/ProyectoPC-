import random

# Pedir al usuario los valores m y n
m = int(input("Ingrese el número de filas (m): "))
n = int(input("Ingrese el número de columnas (n): "))

# Crear una matriz de tamaño m x n con valores aleatorios entre -20 y 20
matriz = [[random.randint(-20, 20) for _ in range(n)] for _ in range(m)]
print("Matriz original:")
for fila in matriz:
    print(fila)

# Crear la matriz traspuesta
matriz_traspuesta = [[matriz[j][i] for j in range(m)] for i in range(n)]
print("Matriz traspuesta:")
for fila in matriz_traspuesta:
    print(fila)