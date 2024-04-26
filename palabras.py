def quitar_tildes(frase):
    tildes = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
    for letra_tilde, letra_sin_tilde in tildes.items():
        frase = frase.replace(letra_tilde, letra_sin_tilde)
    return frase

def main():
    frase = input("Ingresa una frase: ")
    palabra = input("Ingresa una palabra para buscar: ")

    # Quitamos tildes de la frase
    frase_sin_tildes = quitar_tildes(frase)

    # Convertimos la palabra y la frase a minúsculas para comparar
    palabra = palabra.lower()
    frase_sin_tildes = frase_sin_tildes.lower()

    # Verificamos si la palabra está en la frase
    if palabra in frase_sin_tildes:
        print("La palabra '{}' sí está en la frase.".format(palabra))
    else:
        print("La palabra '{}' no está en la frase.".format(palabra))

if __name__ == "__main__":
    main()

