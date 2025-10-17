"""Ejercicio 1: Clasificador de edades

Pide al usuario su edad.
Muestra un mensaje según el rango:

Menos de 13 → “Eres un niño.”
Entre 13 y 17 → “Eres adolescente.”
Entre 18 y 64 → “Eres adulto.”
65 o más → “Eres jubilado."""

edad = int(input("Que edad tienes?: "))

if edad < 13:
    print("Eres un niño.")
elif edad >= 13 and edad < 18:
    print("Eres adolescente.")
elif edad >= 18 and edad < 65:
    print("Eres adulto.")
else:
    print("Eres jubilado.")


"""Ejercicio 2: Calificación de nota.

Pide una nota (del 0 al 10).

0 - 4 → “Suspenso.”
5 - 6 → “Aprobado.”
7 - 8 → “Notable.”
9 - 10 → “Sobresaliente.”

Cualquier otro valor → “Nota no válida.”
Aquí ves cómo controlar también valores incorrectos."""

nota = int(input("¿Qué nota has sacado en el examen?: "))

if nota < 5:
    print("Estás suspendido.")
elif 5 <= nota < 7:
    print("Aprobado.")
elif 7 <= nota < 9:
    print("Notable.")
elif 9 <= nota <= 10:
    print("Sobresaliente.")
else:
    print("Nota no válida.")

"""Ejercicio 3: Clasificador de temperaturas

Pide al usuario que introduzca la temperatura actual en grados Celsius
y muestra un mensaje según el rango en el que se encuentre:

Temperatura	Mensaje que debe mostrar
Menos de 0	"Hace mucho frío, abrígate bien."
De 0 a 15	"Hace fresco, lleva chaqueta."
De 16 a 25	"El clima es agradable."
De 26 a 35	"Hace calor, hidrátate."
Más de 35	"Mucho calor, evita salir al sol." """

temperatura = int(input("¿Que temperatura hace hoy?: "))

if temperatura < 0 :
    print("Hace mucho frío, abrígate bien.")
elif 0 <= temperatura <= 15: 
    print ("Hace fresco, lleva chaqueta.")
elif 16 <= temperatura <= 25: 
    print ("El clima es agradable.")
elif 26 <= temperatura <= 35: 
    print ("Hace calor, hidrátate.")
else : print ("Mucho calor, evita salir al sol.")

