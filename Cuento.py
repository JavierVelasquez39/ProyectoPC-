import turtle

# Variable global para rastrear el estado de la ventana
window_open = True

def on_close():
    global window_open
    window_open = False

# Función para dibujar un panel
def dibujar_panel(window, secuencia):
    try:
        pen = turtle.Turtle()
        pen.speed(0)  # Velocidad más rápida de dibujo
        pen.penup()
        pen.goto(-300, 0)  # Posición inicial del lápiz
        pen.pendown()

        pen.clear()  # Borrar los dibujos anteriores

        # Dibujar figuras basadas en la secuencia
        if secuencia == 1:
            # Dibujar un triángulo
            pen.color("blue")
            pen.begin_fill()
            for _ in range(3):
                pen.forward(100)
                pen.left(120)
            pen.end_fill()
        elif secuencia == 2:
            # Dibujar un cuadrado
            pen.color("red")
            pen.begin_fill()
            for _ in range(4):
                pen.forward(100)
                pen.left(90)
            pen.end_fill()
        elif secuencia == 3:
            # Dibujar un círculo
            pen.color("green")
            pen.begin_fill()
            pen.circle(50)
            pen.end_fill()
        # Add more conditions here for other sequences

        pen.hideturtle()

    except turtle.Terminator:
        on_close()

# Función para mostrar una secuencia
def mostrar_secuencia(window, titulo, narrativa, secuencia):
    print("*********************")
    print(titulo)
    print("*********************")
    print(narrativa)
    dibujar_panel(window, secuencia)

# Función para generar la narrativa basada en los datos del niño
def generar_narrativa(nombre, edad, color_favorito):
    narrativas = [
        f"Había una vez un niño llamado {nombre}, que tenía {edad} años. Un día, mientras paseaba por un bosque lleno de árboles verdes como su color favorito, {color_favorito}, se encontró con una sorpresa inesperada...",
        f"La sorpresa era un {color_favorito} pájaro que hablaba. El pájaro le dijo a {nombre} que estaba perdido y necesitaba ayuda para encontrar su camino a casa...",
        f"{nombre}, siendo un niño amable y valiente, decidió ayudar al pájaro. Juntos, se embarcaron en una emocionante aventura a través del bosque...",
        f"En su viaje, {nombre} y el pájaro se encontraron con muchos desafíos. Pero con cada desafío que superaban, su amistad se hacía más fuerte...",
        f"Finalmente, después de muchos días y noches, {nombre} y el pájaro llegaron a la casa del pájaro. El pájaro agradeció a {nombre} y le prometió que siempre serían amigos...",
        f"Y así, {nombre} volvió a casa, sabiendo que había hecho un nuevo amigo y vivido una increíble aventura. Y cada vez que veía el color {color_favorito}, recordaba a su amigo el pájaro..."
    ]
    return narrativas

# Función principal
def main():
    # Solicitar datos del niño
    nombre = input("Ingrese el nombre del niño: ")
    edad = input("Ingrese la edad del niño: ")
    color_favorito = input("Ingrese el color favorito del niño: ")

    # Generar la narrativa
    narrativa = generar_narrativa(nombre, edad, color_favorito)

    # Crear la ventana de turtle
    window = turtle.Screen()
    window.bgcolor("white")

    # Menú para navegar las secuencias
    while True:
        if window_open:
            opcion = input("\nIngrese el número de secuencia que desea visualizar (1-5), o 'q' para salir: ")
            if opcion.lower() == 'q':
                break
            elif opcion.isdigit() and 1 <= int(opcion) <= 5:
                window.title(f"Panel Secuencia {opcion}")
                mostrar_secuencia(window, f"Secuencia {opcion}", narrativa[int(opcion) - 1], int(opcion))
            else:
                print("Opción no válida. Por favor, ingrese un número del 1 al 5 o 'q' para salir.")
        else:
            print("Por favor, cierre la ventana actual antes de seleccionar otra secuencia.")

if __name__ == "__main__":
    main()
