def limpiar_alturas(altura):

    nueva_lista = []

    for elemento in altura:

        if not isinstance (elemento,str):
            continue

        # este permite tanto strings como números enteros reales
        try:
            altura = float(elemento)
        except:
            continue

        nueva_lista.append(altura)

    return nueva_lista

print (limpiar_alturas([ "1.55" , "1.67" , "1.85" , None, 2 ]))