import math

def calcular_ancho_pentagono(L):
    return L * math.sqrt((5 + 2*math.sqrt(5)) / 2)

L = 7.493875274
ancho = calcular_ancho_pentagono(L)

print(f"El ancho del pentágono es: {ancho}")