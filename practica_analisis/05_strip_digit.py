"""Ejercicios para .strip() y .isdigit()
Dada la lista: 

lista = [" 50 ", "abc", "  300", "20euros", "70", "   ", ""]
Crea una funcion que devuelva: [50, 300, 70]
"""

def filtrar_enteros(lista):
    new_list = []

    for elemento in lista:
        # Trabajamos solo con strings
        if isinstance(elemento, str):
            texto = elemento.strip()  # quitamos espacios

            # Ignoramos los vacíos: "" o "   "
            if texto == "":
                continue

            # Solo aceptamos valores que sean todo dígitos
            if texto.isdigit():
                numero = int(texto)   # convertimos a int
                new_list.append(numero)

    return new_list


print(filtrar_enteros([" 50 ", "abc", "  300", None, "20euros", "70", "   ", ""]))


"""EJERCICIO 2 — Practicar isinstance()

Quiero una función:

def contar_strings(lista):


Que cuente cuántos elementos de la lista son strings, usando isinstance(x, str).

Ejemplo:

["hola", 10, None, "adios", True, "python"]


Debe devolver:

3


👉 Este ejercicio está centrado SOLO en:
isinstance()

🧪 EJERCICIO 3 — Practicar .append() correctamente

Crea una función:

def filtrar_no_vacios(lista):


Que devuelva una lista con solo los strings no vacíos después de .strip().

Ejemplo:

["hola", "   ", "", "mundo"]


Debe devolver:

["hola", "mundo"]


👉 Este ejercicio está centrado en solo:
.strip() → condición → .append()"""
