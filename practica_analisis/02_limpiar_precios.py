"""EJERCICIO 2:  Filtrar y limpiar lista de precios.

Crear una función llamada limpiar_precios() que:
Recorra la lista precios
Ignore: "-" , "N/A", "abc" , None.
Quite espacios si los hay (solo .strip())
Ignore valores que contengan texto al final como "700€"
Convierta los valores válidos a int
Devuelva la lista final de precios limpios"""

precios = ["100", "200", "-", "N/A", "350", "abc", "500", " 600 ", None, "700€"]

def limpiar_precios():
    limpios = []

    for precio in precios:
        if isinstance (precio,str):
            if precio is None: 
                continue
            if precio in ["-", "N/A", "abc"]:
                continue
        
        texto = precio.strip()
        if "€" in texto:
            continue


        limpios.append(int(precio))
    
    return limpios

print(limpiar_precios())


