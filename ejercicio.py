def n_primo(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    inicio = int(input("Por favor, introduce el inicio del rango: "))
    final = int(input("Por favor, introduce el final del rango: "))

    n_primos = [num for num in range(inicio, final+1) if n_primo(num)]

    print(f"Hay {len(n_primos)} números primos dentro del rango especificado. Los números primos son: ")
    for primos in n_primos:
        print(primos)

if __name__ == "__main__":
    main()
