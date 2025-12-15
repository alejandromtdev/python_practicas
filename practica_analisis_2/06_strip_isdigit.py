"""Ejercicio practica de .strip() & .isdigit():

Dada la lista: lista = [" 50 ", "abc", "  300", "20euros", "70", "   ", ""]
Crea una funcion que devuelva: [50, 300, 70]"""

def limpieza_numeros(valores):
    lista_limpia = []
    for numeros in valores:
        if isinstance (numeros,str):
            texto = numeros.strip()
            if not texto.isdigit():
                continue
            limpios = int(texto)
            lista_limpia.append(limpios)
    return (lista_limpia)
print(limpieza_numeros([" 50 ", "abc", "  300", "20euros", "70", "   ", ""]))