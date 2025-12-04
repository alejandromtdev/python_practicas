"""Ejercicio: limpiar enteros de una lista

datos = ["10", "abc", " 20 ", "", None, "30euros", "40", "   ", "N/A", "50"]

Crea una función llamada:
def extraer_enteros(lista):

La función debe:

Recibir una lista como parámetro.
Crear una lista nueva donde guardar valores válidos.
Recorrer la lista con un for.
Ignorar valores: None, "" (cadena vacía), " " (cadena con solo espacios) y "N/A"
Quitar espacios con .strip() en los valores que sean strings.
Conservar solo los valores que sean 100% dígitos, usando .isdigit().
Convertirlos a int.
Guardarlos en la lista nueva.
Al final, devolver la lista limpia de números enteros."""

def extraer_enteros(lista):
    lista_enteros = []
    for listado in lista:
        if listado is None:
            continue
        if isinstance(listado,str):
            texto = listado.strip()
            if texto == "" or texto == "N/A":
                continue
            valores = texto.isdigit()
            valores = int(texto)
        lista_enteros.append(texto)

    return lista_enteros

print (extraer_enteros(["10", "abc", " 20 ", "", None, "30euros", "40", "   ", "N/A", "50"]))