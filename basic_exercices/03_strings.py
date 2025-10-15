"""Ejercicio 1

Crea tres variables tipo string: nombre, apellido y ciudad.
Muestra cada una por pantalla.
Usa type() para comprobar que efectivamente son del tipo str"""

nombre = "Alejandro"
apellido = "Morillas"
ciudad = "Valencia"

print (f"Mi nombre es {nombre} {apellido} y vivo en la ciudad de {ciudad}")

print(type(nombre))
print(type(apellido))
print(type(ciudad))

""" Ejercicio 2

Usa una variable con un texto (una frase tuya).
Aplica los distintos métodos y muestra los resultados.

.upper() → convierte a mayúsculas
.lower() → convierte a minúsculas
.title() → pone mayúscula en la primera letra de cada palabra
.strip() → elimina espacios sobrantes
.replace("a", "o") → cambia letras o palabras
.count("a") → cuenta cuántas veces aparece algo"""

texto = "Aprendiendo strings con python"

print (texto.upper())
print (texto.lower())
print (texto.title())
print (texto.strip())
print (texto.replace("strings","numbers"))
print (texto.count("o"))