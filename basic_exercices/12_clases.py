"""Ejercicio “RegistroNotas”

Crea una clase RegistroNotas que:
Al iniciarse, reciba un nombre_alumno y opcionalmente 
una lista de notas (puede empezar vacía).

Métodos:

agregar_nota(nota) → añade una nota válida (0 al 10). 
Si es inválida, no la añadas (luego haremos manejo de errores).
promedio() → devuelve la media de las notas, o None si no hay.
aprobado() → devuelve True si el promedio ≥ 5, si no False.
mejores_que(valor) → devuelve una lista con las notas > valor."""

class RegistroNotas:
    def __init__(self, nombre_alumno, lista_notas=None):
        self.nombre_alumno = nombre_alumno
        if lista_notas is None:
            self.lista_notas = []
        else:
            self.lista_notas = lista_notas

    def agregar_nota(self, nota):
        if 0 <= nota <= 10:
            self.lista_notas.append(nota)
            print(f"Nota {nota} añadida correctamente.")
        else:
            print("Nota inválida, debe estar entre 0 y 10.")

    def promedio(self):
        if len(self.lista_notas) == 0:
            return None
        return sum(self.lista_notas) / len(self.lista_notas)


