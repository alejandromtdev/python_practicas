"""DICCIONARIOS 

EJERCICIO: 

Para cada producto, muestra un mensaje con(f"...."):

"El producto Portátil Lenovo ha vendido 3 unidades a 1200€ cada una"

1.Calcula para cada producto el ingreso total generado ese día
(precio x unidades_vendidas)
y muestra algo como: "Portátil Lenovo ha generado 3600€ en total hoy"

2. Calcula el ingreso total de toda la tienda sumando todos los ingresos de todos los productos, 
y al final imprime:    "Ingreso total de la tienda hoy: XXXX€"

3. Filtra solo la categoría "Electrónica" y muestra sus productos, pero ojo:
Solo imprime aquellos productos electrónicos que hayan vendido más de 2 unidades.

Frase ejemplo:  "Monitor Samsung es Electrónica y ha vendido 5 unidades (OK)"

4. Encuentra qué producto ha generado más dinero en total (precio x unidades_vendidas)
e imprime:

"El top ventas en ingresos es XXXXX con YYYYY€ """

ventas = [
    {"producto": "Portátil Lenovo", "precio": 1200, "unidades_vendidas": 3, "categoria": "Electrónica"},
    {"producto": "Ratón Logitech", "precio": 40, "unidades_vendidas": 15, "categoria": "Periféricos"},
    {"producto": "Monitor Samsung", "precio": 300, "unidades_vendidas": 5, "categoria": "Electrónica"},
    {"producto": "Teclado Corsair", "precio": 100, "unidades_vendidas": 7, "categoria": "Periféricos"},
    {"producto": "Cable HDMI", "precio": 10, "unidades_vendidas": 20, "categoria": "Accesorios"}
]

for venta in ventas: 
    total_ventas = venta['precio'] * venta['unidades_vendidas']
    print(f"El {venta['producto']} ha generado un total de:{total_ventas}€")

conjunto_ventas = 0

for venta in ventas: 
    conjunto_ventas += venta['precio'] * venta['unidades_vendidas']
print(f"Ingreso total de la tienda hoy: {conjunto_ventas} €")

for venta in ventas:
    if venta ["unidades_vendidas"] > 2 and venta["categoria"] == "Electrónica" :
        print (f"{venta['producto']} es Electrónica  y ha vendido {venta['unidades_vendidas']} unidades (OK)")

mayor_ingreso = 0
producto_top = ""

for venta in ventas:
    total_ventas = venta['precio'] * venta['unidades_vendidas']
    
    if total_ventas > mayor_ingreso:
        mayor_ingreso = total_ventas
        producto_top = venta['producto']

print(f"El top ventas en ingresos es {producto_top} con {mayor_ingreso}€")
