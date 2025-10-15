""" Ejercicio 1: Crear variables simples

Crea varias variables con distintos tipos de datos (por ejemplo:
texto, número y valor lógico) y muestra su contenido por pantalla."""

mi_variable_string = "variable tipo string"
mi_variable_number = 5
mi_variable_decimal = 1.4
mi_variable_boolean = True


print(type(mi_variable_string))
print(type(mi_variable_number))
print(type(mi_variable_decimal))
print(type(mi_variable_boolean))


"""Ejercicio 2: Reasignar valores

Crea una variable con un valor inicial, muéstrala, 
luego cambia su valor por otro y vuelve a mostrarla."""

nombre_persona = "Alejandro"
print(nombre_persona)

nombre_persona = "Juan" 
print(nombre_persona)

"""Ejercicio 3: Nombrar variables correctamente

Crea tres variables con nombres descriptivos 
Ej: nombre, edad, ciudad) y muestra sus valores en pantalla."""

nombre = "Alex"
edad = 35
ciudad = "Valencia"

print(f"Hola mi nombre es {nombre}, tengo {edad} años, y vivo en la ciudad de {ciudad}.")