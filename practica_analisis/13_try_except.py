"""EJERCICIO Try/Except para convertir decimales

Dada esta lista: alturas = ["1.75", " 1.80 ", "abc", "1.6m", None, "dos", "1.90", 2]
Crea una función llamada: def limpiar_alturas(lista):
La función debe: Recorrer la lista, Ignorar valores como: None,  strings que no se puedan convertir a número,
texto sucio como “abc” o “1.6m”,

Convertir a float SOLO los valores válidos
Guardarlos en una nueva lista
Devolver esa lista
Resultado esperado: [1.75, 1.80, 1.90, 2.0]"""

def limpiar_alturas(alturas):
    resultado = []

    for elemento in alturas:
        if elemento is None:
            continue
        if isinstance(elemento,str):
            texto = elemento.strip()
        else: 
            texto = elemento
            
        try :
            numero= float(texto)
        except: 
            continue

        resultado.append(numero)

    return resultado
print (limpiar_alturas(["1.75", " 1.80 ", "abc", "1.6m", None, "dos", "1.90", 2]))