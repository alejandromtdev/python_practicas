"""Ejercicio 4: limpiar enteros de una lista

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

def extraer_enteros (datos):
    valores_validos = []
    for valor in datos:
        if isinstance(valor,str):
            texto = valor.strip()
            if texto.isdigit():
                valores = int(texto)
                valores_validos.append(valores)
    return (valores_validos)
print(extraer_enteros(["10", "abc", " 20 ", "", None, "30euros", "40", "   ", "N/A", "50"]))