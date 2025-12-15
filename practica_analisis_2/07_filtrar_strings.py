"""Ejercicio 07: Filtrar strings válidos con .strip()

Dada esta lista: nombres = 
Crea una función: def limpiar_nombres(lista):
Ignorar: None, strings vacíos después de .strip(), strings que sean "###"
A todos los strings:
aplicar .strip() antes de evaluar nada
Guardar en una nueva lista solo los nombres válidos.
Devolver esa lista.
Resultado esperado: ["Ana", "Luis", "Pedro", "Marta", "Juan"]"""

def filtrar_strings(lista):
    lista_strings = []
    for elemento in lista:
        if isinstance (elemento,str):
            texto = elemento.strip()
            if not texto.isalpha():
                continue
            lista_strings.append(texto)
    return (lista_strings)
print(filtrar_strings(["   Ana", "Luis  ", "   ", "", None, "Pedro", "  Marta", "###", "Juan"]))