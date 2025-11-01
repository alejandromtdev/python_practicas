"""EJERCICIO 1  

Crea una función llamada calcular_media que reciba una lista de números 
(por ejemplo [10, 20, 30, 40]) y devuelva la media aritmética de esos números.
Ademas si la lista esta vacia que entregue None. """

def calcular_media(lista):
    if len(lista) == 0:
        return None    #si me pasas una lista vacia devuelve None (Nada)
    media = sum(lista) / len(lista)
    return media
print(calcular_media([10, 20, 30]))
print(calcular_media([]))

"""EJERCICIO 2 
Crea una función llamada filtrar_mayores_media que reciba una lista de números 
y devuelva una nueva lista con solo los números que están por encima de la media."""

def filtrar_mayores_media(listado):
    media = sum(listado) / len(listado)
    mayores = []
    for numero in listado:
        if numero > media:
            mayores.append(numero)
    return mayores

resultado = filtrar_mayores_media([10, 20, 30, 40, 50])
print(resultado)

"""Qué pasa cuando se ejecuta

La función recibe [10, 20, 30, 40, 50]
Calcula la media: (10 + 20 + 30 + 40 + 50) / 5 = 30
Crea una lista vacía: mayores = []

Empieza el bucle:

10 → no es > 30 → no lo mete
20 → no es > 30 → no lo mete
30 → no es > 30 → no lo mete
40 → sí es > 30 → lo mete
50 → sí es > 30 → lo mete

Termina el bucle y mayores ahora vale [40, 50]
Hace return mayores → devuelve [40, 50]
En el print, se muestra:"""

"""EJERCICIO 3

Crea una función llamada contar_mayores_que que reciba una lista de números y un valor límite.
La función debe devolver cuántos números de la lista son mayores que ese valor."""

def contar_mayores(lista, limite):
    contador = 0                 # Empezamos con 0
    for numero in lista:         # Recorremos la lista
        if numero > limite:      # Si el número es mayor que el límite...
            contador += 1        # ...sumamos 1
    return contador              # Al final, devolvemos el total

resultado = contar_mayores([10, 20, 30, 40, 50], 25)
print(resultado)

"""En este ejercicio, que hacemos?

lista = [10, 20, 30, 40, 50]
limite = 25

Empieza contador = 0

Recorre los números:

10 > 25? ❌ → contador sigue 0
20 > 25? ❌ → contador sigue 0
30 > 25? ✅ → contador = 1
40 > 25? ✅ → contador = 2
50 > 25? ✅ → contador = 3

return contador → devuelve 3 """

"""Ejercicio 4:

Crea una función llamada contar_menores_media 
que reciba una lista de números y devuelva 
cuántos de ellos están por debajo de la media."""

def contar_menores_media(lista):
    media = sum(lista) / len(lista)  # Calcula la media
    contador = 0                     # Empieza el contador en 0
    for numero in lista:             # Recorre cada número
        if numero < media:           # Si es menor que la media...
            contador += 1            # ...suma 1
    return contador                  # Devuelve el total

resultado = contar_menores_media([10, 20, 30, 40, 50])
print(resultado)  # Debería mostrar 2

"""En este ejercicio, hacemos: 

Calcula la media: (10 + 20 + 30 + 40 + 50) / 5 = 30

Empieza el contador en 0
Recorre los números:

10 < 30 → ✅ contador = 1
20 < 30 → ✅ contador = 2
30 < 30 → ❌ igual, no menor → contador = 2
40 < 30 → ❌
50 < 30 → ❌

Termina el bucle → devuelve 2
En pantalla verás: 2 """