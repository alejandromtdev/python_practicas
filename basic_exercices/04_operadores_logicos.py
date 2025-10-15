"""Ejercicio 1:

Crea dos variables, por ejemplo edad y nacionalidad.
Usa un if con and para comprobar si una persona cumple 
ambas condiciones (por ejemplo: tener más de 18 años y ser española).
Muestra un mensaje si se cumplen, y otro si no"""

edad = int(input("Introduce tu edad: "))
nacionalidad = input("Introduce tu nacionalidad: ")

if edad >= 18 and nacionalidad == "Española": 
    print("Tienes acceso a la prestación")
else: print("No tienes acceso, lo siento")

"""Ejercicio 2:

Usa un if con or para verificar, por ejemplo, 
si alguien tiene acceso porque es admin o tiene invitación.
Muestra un mensaje si puede acceder, y otro si no."""

acceso_admin = input("¿Tienes acceso como administrador (si/no)?: ").lower() == "si"
acceso_invitacion = input("¿Tienes invitación (si/no)?: ").lower() == "si"

if acceso_admin or acceso_invitacion:
    print("Puedes acceder al sistema.")
else:
    print("No tienes acceso. Necesitas invitación o ser administrador.")

"""Ejercicio 3: 

Crea una variable booleana (por ejemplo registrado = False).

Usa not para comprobar si no está registrado y mostrar un mensaje acorde.
Cambia el valor a True y vuelve a probar """

registro = input("Estas registrado en nuestro sistema (si/no)?: ").lower() == "si"

if not registro : 
    print("No estás registrado. Por favor, crea una cuenta.")
else:
    print("Bienvenido de nuevo, gracias por iniciar sesión.") 

"""Queremos dejar entrar a un usuario si:

Está registrado, o tiene una invitación válida,
pero además debe no estar bloqueado

Todas se resuelven igual que en los ejercicios 
anteriores (con input().lower() == "si"):

registro → si el usuario está registrado.
invitacion → si tiene invitación.
bloqueado → si está bloqueado."""

registro = input("¿Estás registrado en nuestro sistema (si/no)?: ").lower() == "si"
invitacion = input("¿Dispones de invitación (si/no)?: ").lower() == "si"
bloqueo = input("¿Estás bloqueado en nuestro sistema (si/no)?: ").lower() == "si"

if registro or invitacion:
    if not bloqueo:
        print("Enhorabuena, tienes acceso al sistema.")
    else:
        print("Lo siento, estás bloqueado y no puedes acceder.")
else:
    print("No tienes acceso. Debes estar registrado o tener invitación.")




