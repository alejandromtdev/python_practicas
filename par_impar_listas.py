numero_uno = int(input("introduce un numero: "))
numero_dos = int(input("introduce un segundo numero: "))
numero_tres = int(input("introduce un tercer numero: "))
numero_cuatro = int(input("introduce un cuarto numero: "))
numero_cinco = int(input("introduce un quinto numero: "))

listado_numeros = [numero_uno , numero_dos, numero_tres, numero_cuatro, numero_cinco ]

for listado in listado_numeros: 
    if listado % 2 == 0:
        print(f"{listado} es un numero par")
    else : 
        print(f"{listado} es un numero impar")


