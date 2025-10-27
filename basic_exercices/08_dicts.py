"""Ejercicio 1:

Tienes la siguiente información sobre un producto en una tienda:

nombre: "Portátil Lenovo"
precio: 1200
stock: 15
categoría: "Electrónica"

Crea un diccionario llamado producto con esa información.
Muestra por pantalla el valor de cada clave con un mensaje descriptivo.
(Ejemplo: “El producto cuesta X euros”).
Modifica el valor de stock restando 3 unidades (simulando que se han vendido).
Agrega una nueva clave llamada descuento con el valor 0.1 (representa un 10%).
Calcula el nuevo precio del producto aplicando el descuento y muéstralo."""


producto = {
    "nombre" : "Portátil Lenovo" ,
    "precio" : 1200 ,
    "stock" : 15 ,
    "categoría" : "Electrónica"
}

print (f"El producto es un ordenador {producto['nombre']}, tiene un precio de {producto['precio']}, actualmente tenemos un stock de {producto['stock']} unidades, y esta dentro de la categoria de {producto['categoría']}")

producto ["stock"] = 12

print (producto)

producto ["descuento"] = 0.1

print (producto)

cantidad_descontada = producto["precio"] * producto["descuento"]
precio_final = (producto["precio"] - cantidad_descontada)

producto["precio_con_descuento"] = precio_final

print(producto)

"""Ejercicio 2

Muestra el nombre y precio de cada producto.
Calcula el valor total del stock de cada producto (precio x stock) y muéstralo.
Calcula el valor total de todo el inventario (la suma de todos los valores de stock).
Muestra solo los productos cuya categoría sea "Electrónica"
Calcula cuál es el producto más caro y muestra su nombre y precio."""

productos = [
    {"nombre": "Portátil Lenovo", "precio": 1200, "stock": 12, "categoria": "Electrónica"},
    {"nombre": "Ratón Logitech", "precio": 40, "stock": 50, "categoria": "Periféricos"},
    {"nombre": "Monitor Samsung", "precio": 300, "stock": 20, "categoria": "Electrónica"},
    {"nombre": "Teclado Corsair", "precio": 100, "stock": 30, "categoria": "Periféricos"},
]

for producto in productos:
    valor_total = producto["precio"] * producto["stock"]
    print(f"{producto['nombre']} → valor total del stock: {valor_total}€")

valor_inventario = 0 

for producto in productos:
    valor_inventario += producto["precio"] * producto["stock"]

print(f"El inventario total del lote es: {valor_inventario} €") 

"""Si el print lo ponemos dentro de loop, nos imprimira los valores de cada producto, 
si lo ponemos fuera, obtienes el total del inventario."""

for producto in productos:
    if producto["categoria"] == "Electrónica":
        print(producto["nombre"], producto["precio"])

mas_caro = productos[0]

for producto in productos:
    if producto["precio"]> mas_caro["precio"]:
        mas_caro = producto
    print(f"El producto más caro es {mas_caro['nombre']} con un precio de {mas_caro['precio']}€")

"""Ejercicio de diccionarios

Tienes la siguiente lista de empleados de una empresa:

Muestra el nombre y salario de cada empleado.
Calcula el salario medio de todos los empleados.
Muestra solo los empleados del departamento "Ventas".
Calcula quién gana más y muestra su nombre y salario."""

empleados = [
    {"nombre": "Ana", "departamento": "Ventas", "salario": 2500},
    {"nombre": "Luis", "departamento": "Marketing", "salario": 2300},
    {"nombre": "Marta", "departamento": "Ventas", "salario": 2800},
    {"nombre": "Carlos", "departamento": "IT", "salario": 3000},
    {"nombre": "Lucía", "departamento": "Marketing", "salario": 2100}
]

for empleado in empleados:
    print(f"El nombre del empleado es {empleado['nombre']} y el salario es de: {empleado['salario']}€")

suma_salarios = 0

for empleado in empleados:
    suma_salarios += empleado["salario"]

sueldo_medio = suma_salarios / len(empleados)

print(f"El salario medio de los empleados es de {sueldo_medio}€")

for empleado in empleados:
    if empleado["departamento"] == "Ventas":
        print(f"Los empleados que pertenecen al departamento de Ventas son: {empleado['nombre']}")

empleado_max = empleados[0]  # suponemos que el primero es el que más gana

for empleado in empleados:
    if empleado["salario"] > empleado_max["salario"]:
        empleado_max = empleado

print(f"El empleado que más salario gana es {empleado_max['nombre']} con {empleado_max['salario']}€.")
