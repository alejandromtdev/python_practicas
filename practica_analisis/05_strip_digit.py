"""Ejercicios para .strip() y .isdigit()
Dada la lista: 

lista = [" 50 ", "abc", "  300", "20euros", "70", "   ", ""]
Crea una funcion que devuelva: [50, 300, 70]
"""

def filtrar_enteros(lista):
    new_list = []

    for elemento in lista:
        # Trabajamos solo con strings
        if isinstance(elemento, str):
            texto = elemento.strip()  # quitamos espacios

            # Ignoramos los vacíos: "" o "   "
            if texto == "":
                continue

            # Solo aceptamos valores que sean todo dígitos
            if texto.isdigit():
                numero = int(texto)   # convertimos a int
                new_list.append(numero)

    return new_list


print(filtrar_enteros([" 50 ", "abc", "  300", None, "20euros", "70", "   ", ""]))


"""EJERCICIO 2 — Practicar isinstance()

Quiero una función:

def contar_strings(lista):
Que cuente cuántos elementos de la lista son strings, 
usando isinstance(x, str).

Ejemplo: ["hola", 10, None, "adios", True, "python"]
Debe devolver:  3"""

def contar_strings(lista):
    contador = 0   # resultado final

    for elemento in lista:   # elemento va siendo "hola", luego 10, luego None...
        
        # comprobación
        if isinstance(elemento, str):  
            # si es string sumo
            contador = contador + 1

    return contador

print (contar_strings(["hola", 10, None, "adios", True, "python"]))

"""EJERCICIO 3 — Practicar .append() correctamente

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

"""EJERCICIO 4:

Crear una función:
def filtrar_mayusculas(lista):

Que:
Reciba una lista de strings
Haga .strip()
Ignore los vacíos
Devuelva solo los strings que estén en MAYÚSCULAS

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

