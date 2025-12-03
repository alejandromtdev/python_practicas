"""Ejercicio 1: “Filtrar números válidos de una lista.

Escribe una función llamada extraer_numeros() que:
Recorra la lista valores
Ignore: "hola" , "N/A" , None.
Se quede SOLO con los valores numéricos válidos
Los convierta en int
Devuelva una nueva lista con los números"""

valores = ["10", "20", "hola", "30", "N/A", "40", None, "50"]

def extraer_numeros():
    resultado = []
    for datos in valores:
        if datos is None: 
            continue 

        if isinstance (datos,str) and datos in ["hola", "N/A"]:
            continue

        resultado.append(int(datos))
    
    return resultado

print (extraer_numeros()) 

