"""EJERCICIO 11:

Crear una función: def filtrar_mayusculas(lista):
Que: Reciba una lista de strings, haga .strip() ignore los vacíos y 
devuelva solo los strings que estén en MAYÚSCULAS.
Ejemplo: ["  HOLA  ", "mundo", "  ADIOS", "python", "  ", ""]
Debe devolver: ["HOLA", "ADIOS"]"""

def filtrar_mayusculas(lista):
    resultado = []
    for elemento in lista:
            texto = elemento.strip()
            if texto != "" and texto.isupper():
                resultado.append(texto)
    return resultado
print(filtrar_mayusculas(["  HOLA  ", "mundo", "  ADIOS", "python", "  ", ""])) 
