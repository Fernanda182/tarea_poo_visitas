# Clase modelo que representa a un visitante.
# Aquí solo se guardan los datos del visitante.

class Visitante:
    def __init__(self, cedula, nombre_completo, motivo_visita):
        # Atributo: cédula del visitante
        self.cedula = cedula

        # Atributo: nombre completo del visitante
        self.nombre_completo = nombre_completo

        # Atributo: motivo de la visita
        self.motivo_visita = motivo_visita