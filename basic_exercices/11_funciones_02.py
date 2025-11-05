"""Ejercicio 01:

Crea una función llamada estadisticas_basicas 
que reciba una lista de números y devuelva un diccionario con tres claves:

"min" → el valor mínimo
"max" → el valor máximo
"media" → el promedio"""

def estadisticas_basicas(lista):
    if not lista:
        return {"mensaje": "Debes introducir valores."}
    
    resultado = {}
    resultado["min"] = min(lista)
    resultado["max"] = max(lista)
    resultado["media"] = sum(lista) / len(lista)
    
    return resultado
print(estadisticas_basicas([25,35,35]))

"""Ejercicio 02:

Crea una función llamada filtrar_mayores 
que reciba una lista de números y un umbral (threshold),
y devuelva una nueva lista con los valores mayores que ese umbral """

def filtrar_mayores (lista_numeros, threshold):
    lista_mayores = []
    for num in lista_numeros:
        if num >= threshold:
            lista_mayores.append(num)
    return lista_mayores

print (filtrar_mayores([10, 25, 5, 30, 40], 20))

"""Explicación línea a línea. 

Creamos la función filtrar_mayores.
Le decimos que va a recibir dos cosas:

lista_numeros: una lista de números (por ejemplo [10, 25, 5, 30, 40])

threshold: el número “límite” (por ejemplo 20)

lista_mayores = []  Aquí creamos una lista vacía donde guardaremos solo los números 
que sean mayores que threshold y que por ahora está vacía: []

for num in lista_numeros: “para cada número (num) que haya dentro de la lista 
que me pasen (lista_numeros), haz lo siguiente”.

Si la lista es por ejemplo [10, 25, 5, 30, 40], el bucle se repite 5 veces:

1ª vuelta → num = 10
2ª vuelta → num = 25
3ª vuelta → num = 5
4ª vuelta → num = 30
5ª vuelta → num = 40

if num > threshold:  Comprobamos si ese número es mayor que el umbral. Si el threshold es 20:

10 > 20 → ❌ no se cumple
25 > 20 → ✅ sí se cumple
5 > 20 → ❌
30 > 20 → ✅
40 > 20 → ✅

Solo los que cumplen el “sí” pasarán al siguiente paso.

lista_mayores.append(num)

👉 Si el número cumple la condición, lo metemos dentro de la lista usando .append().
Cada vez que un número entra, la lista crece un poco más.

Después de 25 → [25]
Después de 30 → [25, 30]
Después de 40 → [25, 30, 40]

return lista_mayores Cuando el bucle termina (ya revisó todos los números), 
devolvemos la lista con los que superaron el umbral."""
    

"""Version de una sola linea"""

def filtrar_mayores(lista_numeros, threshold):
    return [num for num in lista_numeros if num > threshold]

"""Esto hace exactamente lo mismo, a esto se le denomina una list comprehesion, y nos dice: 

Devuélveme una lista con cada num que venga de lista_numeros solo si num > threshold. """


"""Ejercicio 03:

Crea una función llamada contar_mayores que reciba:

una lista de números
y un valor umbral (threshold)
Y devuelva cuántos números son mayores que el umbral."""

def contar_mayores (lista, theshold):
    contador = 0
    for num in lista:
        if num >= theshold:
            contador +=1
    return contador

print(contar_mayores([25,29,20,34,7,22],20))

"""Ejercicio 04: Normalizar datos numéricos

Crea una función llamada normalizar_datos que reciba una lista de números 
y devuelva una nueva lista donde cada número esté dividido entre el valor máximo de la lista."""

def normalizar_datos(lista_num):
    numero_maximo = max(lista_num)
    nueva_lista = []
    for num in lista_num:
        valor_normalizado = num / numero_maximo
        nueva_lista.append(valor_normalizado)
    return nueva_lista

print(normalizar_datos([10, 20, 30]))


def normalizar_datos(lista_numeros):
    return [num / max(lista_numeros) for num in lista_numeros]

print(normalizar_datos([10, 20, 30]))

"""Version Pro corta: Para cada número (num) que hay en la lista (lista_numeros),
divide ese número entre el valor máximo de la lista,
y devuélveme una nueva lista con todos esos resultados."""


"""Ejercicio 05: Limpiar textos

Crea una función llamada limpiar_textos que reciba una lista de strings (frases o palabras)
y devuelva una nueva lista donde:

Todo el texto esté en minúsculas, no haya espacios al principio ni al final y no haya puntos ni comas. """

def limpiar_textos(lista_strings):
    nueva_lista = []                       # Creamos una lista vacía para guardar los textos limpios
    for texto in lista_strings:                  # Recorremos cada string de la lista original
        texto_limpio = texto.lower().strip().replace(",", "").replace(".", "")  # Limpiamos el texto
        nueva_lista.append(texto_limpio)             # Guardamos el texto limpio en la nueva lista

    return nueva_lista                              # Devolvemos la lista con los textos limpios

print(limpiar_textos(["  Hola,", "Mundo.", "  PYTHON , "]))

""" Creamos nueva_lista = [] fuera del bucle, para que no se reinicie cada vez.

Bucle for: Cada vez que recorremos un elemento (texto), trabajamos con él individualmente.

.lower() → convierte el texto a minúsculas.
.strip() → quita los espacios al principio y final.
.replace(",", "") → elimina las comas (fíjate que ponemos comillas vacías " " si queremos sustituir por nada).
.replace(".", "") → elimina los puntos.
.append() → agrega el resultado limpio a la lista final.

return nueva_lista → devuelve la lista completa, ya limpia."""

""" Ejercicio 06:

Crea una función llamada analisis_numeros que reciba una lista de números
y devuelva un diccionario con esta información:

"cantidad" → cuántos números hay
"suma" → la suma total
"media" → el promedio
"minimo" → el valor más pequeño
"maximo" → el valor más grande
"ordenados" → la lista ordenada de menor a mayor
"mayores_que_media" → una lista con los valores que son mayores que la media"""

def analisis_numeros(lista_numeros):
    resultado = {}  # Creamos un diccionario donde guardaremos los resultados
    
    cantidad = len(lista_numeros)       # Cuántos elementos hay
    suma = sum(lista_numeros)           # Suma total
    media = suma / cantidad             # Media aritmética
    minimo = min(lista_numeros)         # Valor mínimo
    maximo = max(lista_numeros)         # Valor máximo
    ordenados = sorted(lista_numeros)   # Lista ordenada
    
    mayores_que_media = [num for num in lista_numeros if num > media]  # Filtramos los mayores que la media
    
    # Guardamos todo en el diccionario
    resultado["cantidad"] = cantidad
    resultado["suma"] = suma
    resultado["media"] = media
    resultado["minimo"] = minimo
    resultado["maximo"] = maximo
    resultado["ordenados"] = ordenados
    resultado["mayores_que_media"] = mayores_que_media
    
    return resultado  # Devolvemos el diccionario completo


print(analisis_numeros([10, 20, 30, 40, 50]))


