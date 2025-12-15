"""EJERCICIO 2:  Filtrar y limpiar lista de precios.

Crear una función llamada limpiar_precios() que:
Recorra la lista precios
Ignore: "-" , "N/A", "abc" , None.
Quite espacios si los hay (solo .strip())
Ignore valores que contengan texto al final como "700€"
Convierta los valores válidos a int
Devuelva la lista final de precios limpios"""

precios = ["100", "200", "-", "N/A", "350", "abc", "500", " 600 ", None, "700€"]

def limpiar_precios (precios):
    resultado = []
    for elemento in precios:
        if not isinstance (elemento,str):
            continue
        texto = elemento.strip()
        if not texto.isdigit():
            continue
        resultado.append(int(texto))
    return resultado

print (limpiar_precios(["100", "200", "-", "N/A", "350", "abc", "500", " 600 ", None, "700€"]))

"""y si quisieramos meter el 700€ como 700???"""

def limpiar_precios(precios):
    resultado = []

    for elemento in precios:
        if not isinstance(elemento, str):
            continue

        texto = elemento.strip()
        solo_numeros = ""

        for c in texto:
            if c.isdigit():
                solo_numeros += c

        if solo_numeros == "":
            continue

        resultado.append(int(solo_numeros))

    return resultado


print (limpiar_precios(["100", "200", "-", "N/A", "350", "abc", "500", " 600 ", None, "700€"]))