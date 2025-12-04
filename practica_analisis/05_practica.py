"""Ejercicio 1 — Filtrar valores numéricos sencillos

Dada esta lista: valores = ["15", "hola", "25", None, "N/A", "40", "xyz", "50"]
Crea una función llamada: def extraer_numeros_validos():
La función debe: Recorrer la lista valores.
Ignorar: "hola",  "xyz", "N/A", None
Quedarse solo con los valores numéricos válidos.
Convertir los buenos a int.
Devolver una nueva lista con los números enteros limpios.

Resultado esperado: [15, 25, 40, 50]"""

def extraer_numeros_validos(valores):
    numeros_enteros_limpios = []
    for elemento in valores:
        if elemento is None:
            continue
        if isinstance (elemento,str) and elemento in ["hola","N/A","xyz"]:
            continue
        limpios = int(elemento)
        numeros_enteros_limpios.append(limpios)

    return (numeros_enteros_limpios)

print(extraer_numeros_validos(["15", "hola", "25", None, "N/A", "40", "xyz", "50"]))

