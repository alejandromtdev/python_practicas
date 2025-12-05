"""EJERCICIO 9 — Practicar isinstance()

Quiero una función:

def contar_strings(lista):
Que cuente cuántos elementos de la lista son strings, 
usando isinstance(x, str).

Ejemplo: ["hola", 10, None, "adios", True, "python"]
Debe devolver:  3"""

def contar_strings(lista):
    contador = 0   # resultado final

    for elemento in lista:   # elemento va siendo "hola", luego 10, luego None...
        
        # comprobación
        if isinstance(elemento, str):  
            # si es string sumo
            contador = contador + 1

    return contador

print (contar_strings(["hola", 10, None, "adios", True, "python"]))