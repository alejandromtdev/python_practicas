"""Ejercicio 3: Crea una función llamada limpiar_y_sumar(valores) que:

Reciba la lista como parámetro → nada de variables globales. 
Recorra la lista con un for.                                 
Ignore los  valores: None , cadenas vacías, "" ,  "N/A".     
Si el valor es un str, quítale espacios con .strip().
Intenta convertir cada valor a número decimal con float(...).
Si al convertir da error (por ejemplo "abc" o "50euros"), 
usa try/except para ignorarlo (no debe romper el programa).
Ve acumulando (sumando) los valores numéricos válidos en una variable.
la función debe devolver la suma total de todos los números válidos."""

def limpiar_y_sumar(valores):
    total = 0.0                  # variable con la suma de los números válidos ponemos floats. 

    for valor in valores:

        if valor is None:       # Ignoramos el None
            continue

        
        if isinstance(valor, str):      # Si es string...
            texto = valor.strip()       # quitamos espacios inicio y final

            
            if texto == "" or texto == "N/A":       # Ignoramos cadenas vacías y "N/A"  
                continue

            
            try:
                numero = float(texto)       # Intentamos convertir a número con float()
            except ValueError:              # Si falla, como: "abc" o "50euros" , lo ignoramos.
                continue

            
            total += numero                 # Si lo convirtio, sumalo.

    return total


valores = ["10", "25", "abc", "", " 30 ", None, "40.5", "15.2", "N/A", "50euros"]
print(limpiar_y_sumar(valores))