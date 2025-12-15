"""Ejercicio 3: Crea una función llamada limpiar_y_sumar(valores) que:

Reciba la lista como parámetro → nada de variables globales. 
Recorra la lista con un for.                                 
Ignore los  valores: None , cadenas vacías, "" ,  "N/A".     
Si el valor es un str, quítale espacios con .strip().
Intenta convertir cada valor a número decimal con float(...).
Si al convertir da error (por ejemplo "abc" o "50euros"), 
usa try/except para ignorarlo (no debe romper el programa).
Ve acumulando (sumando) los valores numéricos válidos en una variable.
la función debe devolver la suma total de todos los números válidos.

valores = ["10", "25", "abc", "", " 30 ", None, "40.5", "15.2", "N/A", "50euros"]"""


def limpiar_y_sumar(valores):
    total = 0.0
    for valor in valores:
        if isinstance (valor,str):
            texto = valor.strip()
            try: 
                numero = float(texto)
            except ValueError:
                continue
            total += numero
    return (total)
print(limpiar_y_sumar(["10", "25", "abc", "", " 30 ", None, "40.5", "15.2", "N/A", "50euros"]))