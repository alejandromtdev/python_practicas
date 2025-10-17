"""Ejercicio 4: Acceso al evento

Pregunta si el usuario tiene entrada (si/no).

Si tiene entrada, pregunta si es VIP (si/no).
Si es VIP, muestra “Acceso preferente”.
Si no, muestra “Acceso general”.
Si no tiene entrada, muestra “No puedes entrar sin entrada.” """

acceso_evento = input("Tienes entrada para el evento?: ").lower() == "si"
eres_vip = input("Eres VIP?: ").lower() == "si"

if acceso_evento:
    if eres_vip == True : 
        print ("Acceso preferente")
    else: print ("Acceso general")
else : print ("No puedes entrar sin entrada.")

"""Ejercicio: Sistema de Login (verificación de usuario)

Crea dos variables con los datos correctos del sistema (por ejemplo):
Luego pide al usuario que introduzca su nombre de usuario 
y su contraseña mediante input().

Primero comprueba si el nombre de usuario introducido 
coincide con el guardado.
Si no coincide, muestra: "Nombre de usuario incorrecto."

Si sí coincide, entra en un segundo if (anidado) 
para comprobar la contraseña:

Si la contraseña también coincide → "Bienvenido, acceso concedido."

Si la contraseña no coincide → "Contraseña incorrecta." """

usuario_valido = "Alejandro"
contraseña_valida = "python1234"

login = input("Introduce tu usuario: ").lower()
login2 = input("Introduce tu contraseña: ").lower()

if login == usuario_valido : 
    if login2 == contraseña_valida: 
        print("Bienvenido, acceso concedido.")
    else: print("Contraseña incorrecta.")    
else:
    print("Nombre de usuario incorrecto.")
    