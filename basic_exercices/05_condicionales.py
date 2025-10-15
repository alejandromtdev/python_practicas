"""Ejercicio 1: Clasificador de edades

Pide al usuario su edad.
Muestra un mensaje según el rango:

Menos de 13 → “Eres un niño.”
Entre 13 y 17 → “Eres adolescente.”
Entre 18 y 64 → “Eres adulto.”
65 o más → “Eres jubilado."""

edad = int(input("Que edad tienes?: "))

if edad < 13:
    print("Eres un niño.")
elif edad >= 13 and edad < 18:
    print("Eres adolescente.")
elif edad >= 18 and edad < 65:
    print("Eres adulto.")
else:
    print("Eres jubilado.")
