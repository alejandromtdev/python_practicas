"""Ejercicio 6 -  practica de .strip() & .isdigit()
Dada la lista: lista = [" 50 ", "abc", "  300", "20euros", "70", "   ", ""]
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
