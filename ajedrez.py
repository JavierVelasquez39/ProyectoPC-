def validar_color(color):
    return color.lower() in ['blanco', 'negro']

def validar_posicion(posicion):
    return len(posicion) == 2 and 'a' <= posicion[0] <= 'h' and '1' <= posicion[1] <= '8'

Tablero = [[["v"] for _ in range(8)] for _ in range(8)]

color_torre = input("Ingrese el color de la torre (blanco o negro): ").lower().strip()
while not validar_color(color_torre): 
    print("Ingrese un color válido.")
    color_torre = input("Ingrese el color de la torre (blanco o negro): ").lower().strip()

posicion_torre = input("Ingrese la posición de la torre (a1, b2, e4, etc.): ").lower().strip()
while not validar_posicion(posicion_torre):
    print("Ingrese una posición válida.")
    posicion_torre = input("Ingrese la posición de la torre (a1, b2, e4, etc.): ").lower().strip()

fila_torre, col_torre = 8 - int(posicion_torre[1]), ord(posicion_torre[0]) - ord('a')

while Tablero[fila_torre][col_torre][0] != "v":
    print("La posición ya está ocupada, ingrese una nueva posición.")
    posicion_torre = input("Ingrese la posición de la torre (a1, b2, e4, etc.): ")
    fila_torre, col_torre = 8 - int(posicion_torre[1]), ord(posicion_torre[0]) - ord('a')

Tablero[fila_torre][col_torre] = ["Torre", color_torre]

num_piezas = int(input("Ingrese el número de piezas adicionales: "))

for i in range(num_piezas):
    tipo_pieza = input(f"Ingrese el tipo el tipo de pieza {i+1} (alfil, peón, caballo, etc.): ")
    color_pieza = input(f"Ingrese el color de la pieza {i+1} (blanco o negro): ").lower().strip()
    while not validar_color(color_pieza):
        print("Ingrese un color válido.")
        color_pieza = input(f"Ingrese el color de la pieza {i+1} (blanco o negro): ").lower().strip()
    
    posicion_pieza = input(f"Ingrese la posición de la pieza {i+1} (a1, b2, e4, etc.): ").lower().strip()
    while not validar_posicion(posicion_pieza):
        print("Ingrese una posición válida. El formato correcto <Letra><Número>, ej: a1, b2, e4, etc")
        posicion_pieza = input(f"Ingrese la posición de la pieza {i+1} (a1, b2, e4, etc.): ").lower().strip()

    fila_pieza, col_pieza = 8 - int(posicion_pieza[1]), ord(posicion_pieza[0]) - ord('a')

    # Verificar si la posición está ocupada 
    while Tablero[fila_pieza][col_pieza][0] != "v":
        print("La posición ya está ocupada. Ingrese una nueva posición.")
        posicion_pieza = input(f"Ingrese la posición de la pieza {i+1} (a1, b2, e4, etc.): ")
        fila_pieza, col_pieza = 8 - int(posicion_pieza[1]), ord(posicion_pieza[0]) - ord('a')

    Tablero[fila_pieza][col_pieza] = [tipo_pieza, color_pieza]

for fila in Tablero:
    print(fila)

# Evaluación de movimientos 
direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for direccion in direcciones: 
    delta_fila, delta_col = direccion
    fila, col = fila_torre + delta_fila, col_torre + delta_col
    while 0 <= fila < 8 and 0 <= col < 8: 
        if Tablero[fila][col][0] == "v":
            print(f"Posición {chr(col + ord('a'))}{8 - fila}")
            fila, col = fila + delta_fila, col + delta_col
        else: 
            if Tablero[fila][col][1] != color_torre:
                print(f"Posición: {chr(col + ord('a'))}{8 - fila} (Pieza capturable)")
                break 






