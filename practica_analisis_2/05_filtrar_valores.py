"""Ejercicio 5— Filtrar valores numéricos sencillos

Dada esta lista: valores = ["15", "hola", "25", None, "N/A", "40", "xyz", "50"]
Crea una función llamada: def extraer_numeros_validos():
La función debe: Recorrer la lista valores.
Ignorar: "hola",  "xyz", "N/A", None
Quedarse solo con los valores numéricos válidos.
Convertir los buenos a int.
Devolver una nueva lista con los números enteros limpios.

Resultado esperado: [15, 25, 40, 50]"""

def extraer_numeros_validos (valores):
    numeros_validos = []
    for numeros in valores: 
        if not isinstance (numeros,str):
            continue
        texto = numeros.strip()
        if not texto.isdigit():
            continue
        validos = int(texto)
        numeros_validos.append(validos)
    return(numeros_validos)
print(extraer_numeros_validos(["15", "hola", "25", None, "N/A", "40", "xyz", "50"]))