"""Ejercicio 8: Filtrar y limpiar números enteros simples

Dada esta lista: valores = ["100", " 200 ", "", "abc", None, "300euros", "400", "   ", "N/A", "500"]

Crea una función llamada: def extraer_enteros(lista):

La función debe: Recibir la lista por parámetro.
Ignorar: None, cadenas vacías "", cadenas con solo espacios " " (porque tras .strip() quedan vacías), "N/A"
Hacer .strip() a los strings. Mantener solo los valores que sean 100% dígitos usando .isdigit().
Convertirlos a int. Guardarlos en una lista nueva.
Devolver la lista final.
Resultado esperado: [100, 200, 400, 500]"""

def extraer_enteros (valores):
    lista_limpia = []
    for numeros in valores:
        if numeros is None:
            continue
        if not isinstance (numeros,str): 
            continue
        texto = numeros.strip()
        if texto == [""]:
            continue 
        if not texto.isdigit():
            continue
        limpios = int(texto)
        lista_limpia.append(limpios)
    return lista_limpia
    
print(extraer_enteros(["100", " 200 ", "", "abc", None, "300euros", "400", "   ", "N/A", "500"]))