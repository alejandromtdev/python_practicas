#EJERCICIO 1 - LISTAS

#Calcula la edad promedio (sin usar sum() ni len()).

edades = [23, 19, 25, 30, 22, 19, 23, 28, 30, 21, 25, 19]

total_suma = 0      # acumulador de la suma
contador = 0        # contador de elementos

for edad in edades:
    total_suma = total_suma + edad   # sumamos cada edad
    contador = contador + 1          # contamos una más

promedio = total_suma / contador     # sacamos la media
print("El promedio de edades es:", promedio)


#Haz lo mismo pero esta vez usando sum() y len().

edades = [23, 19, 25, 30, 22, 19, 23, 28, 30, 21, 25, 19]

promedio = sum(edades) / len(edades)
print("El promedio de edades es:", promedio)

"""Esta es una manera mas profesional 
de hacerlo ya que python tiene funciones integradas que realizan esas tareas
sum(lista) → devuelve la suma de todos los elementos.
len(lista) → devuelve cuántos elementos hay en la lista."""


#Cuenta cuántas personas tienen más de 25 años.

edades = [23, 19, 25, 30, 22, 19, 23, 28, 30, 21, 25, 19]

contador_mayores = 0

for edad in edades:
    if edad > 25:
        contador_mayores = contador_mayores + 1

print("Hay", contador_mayores, "personas mayores de 25 años.")


#Crea un set con las edades únicas.

edades = [23, 19, 25, 30, 22, 19, 23, 28, 30, 21, 25, 19]

edades_unicas = set(edades)
print(edades_unicas)

"""Otra forma distinta de hacerlo mas manual"""

edades_unicas = set()  # creamos un set vacío

for edad in edades:
    edades_unicas.add(edad)  # .add() agrega solo si no existe ya

print(edades_unicas)

#Muestra la cantidad de edades distintas que aparecen.

print("Cantidad de edades únicas:", len(edades_unicas))


"""Ejercicio 2: Calcula el promedio solo de las notas aprobadas """


notas = [4.5, 7.0, 8.2, 5.9, 3.7, 9.0, 6.5, 4.2, 10.0, 5.0]

suma_aprobados = 0
contador_aprobados = 0

for nota in notas:
    if nota >= 5:
        suma_aprobados = suma_aprobados + nota
        contador_aprobados = contador_aprobados + 1

if contador_aprobados > 0:
    promedio_aprobados = suma_aprobados / contador_aprobados
    print("Promedio de notas aprobadas:", promedio_aprobados)
else:
    print("No hay aprobados.")

"""Ejercicio 3

Calcula: 

La suma total de la lista de ventas.
El promedio diario de ventas.
Cuántos días se vendieron más de 100 unidades."""

ventas = [120, 85, 300, 150, 90, 200, 75, 400, 50, 95]

suma_ventas = sum(ventas)
print (suma_ventas)

promedio = sum(ventas)/ len(ventas) 
print (promedio)

mayores_ventas = 0

for venta in ventas:
    if venta > 100:
        mayores_ventas = mayores_ventas + 1
print(f"Hay {mayores_ventas} mayores de 100")










