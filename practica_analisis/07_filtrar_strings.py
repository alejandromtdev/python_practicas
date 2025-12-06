"""Ejercicio 07: Filtrar strings válidos con .strip()

Dada esta lista: nombres = ["   Ana", "Luis  ", "   ", "", None, "Pedro", "  Marta", "###", "Juan"]
Crea una función: def limpiar_nombres(lista):
Ignorar: None, strings vacíos después de .strip(), strings que sean "###"
A todos los strings:
aplicar .strip() antes de evaluar nada
Guardar en una nueva lista solo los nombres válidos.
Devolver esa lista.
Resultado esperado: ["Ana", "Luis", "Pedro", "Marta", "Juan"]"""

def limpiar_nombres(lista):
    listado_nombres = []
    for elemento in lista:
        if not isinstance(elemento, str):
            continue   # si no es string, pasa al siguiente
        texto = elemento.strip()
        if texto in ["", "###"]:
            continue   # si está vacío o es ###, lo ignoramos
        listado_nombres.append(texto)  # aquí ya es válido
    return listado_nombres
print (limpiar_nombres(["   Ana", "Luis  ", "   ", "", None, "Pedro", "  Marta", "###", "Juan"]))

