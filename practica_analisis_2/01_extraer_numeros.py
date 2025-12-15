"""Ejercicio 1: “Filtrar números válidos de una lista.

Escribe una función llamada extraer_numeros() que:
Recorra la lista valores
Ignore: "hola" , "N/A" , None.
Se quede SOLO con los valores numéricos válidos
Los convierta en int
Devuelva una nueva lista con los números"""



def extraer_numeros (valores):
    lista_limpia = []
    for elemento in valores:
        if not isinstance (elemento,str):
            continue
        if not elemento.isdigit(): 
            continue
        lista_limpia.append(int(elemento))
    return lista_limpia 

print(extraer_numeros(["10", "20", "hola", "30", "N/A", "40", None, "50"]))