for venta in ventas: 
    total_ventas = venta['precio'] * venta['unidades_vendidas']
    print(f"El {venta['producto']} ha generado un total de:{total_ventas}€")

conjunto_ventas = 0

for venta in ventas: 
    conjunto_ventas += venta['precio'] * venta['unidades_vendidas']
    print(f"Ingreso total de la tienda hoy: {conjunto_ventas} €")