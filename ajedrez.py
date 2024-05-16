def crear_tablero(filas, columnas):
    tablero = [['' for _ in range(columnas)] for _ in range(filas)]
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)

def agregar_pieza(tablero, fila, columna, tipo_pieza, color):
    tablero[fila][columna] = (tipo_pieza, color)

def listar_movimientos_torre(tablero, fila_torre, columna_torre):
    movimientos = []
    # Movimientos horizontales
    for columna in range(len(tablero[0])):
        if columna != columna_torre:
            movimientos.append((fila_torre, columna))
    # Movimientos verticales
    for fila in range(len(tablero)):
        if fila != fila_torre:
            movimientos.append((fila, columna_torre))
    return movimientos

def mostrar_movimientos_validos(tablero, fila_torre, columna_torre):
    movimientos = listar_movimientos_torre(tablero, fila_torre, columna_torre)
    for movimiento in movimientos:
        fila, columna = movimiento
        if tablero[fila][columna] == '':
            print(f'{fila}{columna} vacía')
        else:
            tipo_pieza, color = tablero[fila][columna]
            print(f'{fila}{columna} con {tipo_pieza} {color}')

def main():
    filas = 8
    columnas = 8
    tablero = crear_tablero(filas, columnas)

    # Agregar piezas
    cantidad_piezas = int(input("Ingrese la cantidad de piezas a agregar: "))
    for _ in range(cantidad_piezas):
        tipo_pieza = input("Tipo de pieza (alfil, peón, caballo, torre, etc.): ")
        color = input("Color (blanco o negro): ")
        fila = int(input("Fila (número): "))
        columna = int(input("Columna (número): "))
        agregar_pieza(tablero, fila, columna, tipo_pieza, color)

    # Ingresar pieza de torre a evaluar
    print("\nIngrese la pieza de la torre a evaluar:")
    fila_torre = int(input("Fila de la torre: "))
    columna_torre = int(input("Columna de la torre: "))

    # Mostrar movimientos válidos
    print("\nMovimientos válidos de la torre:")
    mostrar_movimientos_validos(tablero, fila_torre, columna_torre)

    # Imprimir matriz
    print("\nEstructura de datos de la matriz:")
    imprimir_tablero(tablero)

if __name__ == "__main__":
    main()
