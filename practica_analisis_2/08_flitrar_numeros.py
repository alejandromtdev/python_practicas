"""Crea una función llamada: def extraer_enteros(lista):

La función debe: 
Ignorar: None, cadenas vacías "", "N/A"
Hacer .strip() a los strings. Mantener solo los valores que sean 100% dígitos.
Convertirlos a int. Guardarlos en una lista nueva.
Devolver la lista final.
Resultado esperado: [100, 200, 400, 500]"""

def extraer_enteros(lista):
    lista_final = []
    for elemento in lista:
        if isinstance (elemento,str):
            texto = elemento.strip()
            if not texto.isdigit():
                continue
            numeros = int(texto)
            lista_final.append(numeros)
    return (lista_final)
print(extraer_enteros(["100", " 200 ", "", "abc", None, "300euros", "400", "   ", "N/A", "500"]))