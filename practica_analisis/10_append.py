"""EJERCICIO 10 — Practicar .append() correctamente

Crea una función:

def filtrar_no_vacios(lista):
Que devuelva una lista con solo los strings no vacíos después de .strip().
Ejemplo:  ["hola", "   ", "", "mundo"]
Debe devolver:  ["hola", "mundo"]  """

def filtrar_no_vacios(lista):
    resultado = []              # 1. lista donde guardaremos los buenos

    for elemento in lista:      # 2. recorremos
        if isinstance(elemento, str):   # 3. trabajar solo con strings
            texto = elemento.strip()     # 4. limpiamos espacios
            if texto != "":             # 5. si NO está vacío...
                resultado.append(texto) # 6. LO AÑADO a la lista final

    return resultado                      # 7. devuelvo la lista limpia

print (filtrar_no_vacios(["hola", "   ", "", "mundo"]))