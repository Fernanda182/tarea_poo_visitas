# Importamos la clase Visitante desde la capa de modelos
from modelos.visitante import Visitante


# Clase de servicio:
# aquí va toda la lógica del CRUD en memoria.
class VisitaServicio:
    def __init__(self):
        # Lista privada donde se almacenan los visitantes
        self.__visitantes = []

    # Método para registrar un nuevo visitante
    def registrar_visitante(self, cedula, nombre_completo, motivo_visita):
        # Limpiamos espacios
        cedula = str(cedula).strip()
        nombre_completo = str(nombre_completo).strip()
        motivo_visita = str(motivo_visita).strip()

        # Validamos campos vacíos
        if not cedula or not nombre_completo or not motivo_visita:
            raise ValueError("Todos los campos son obligatorios.")

        # Validamos cédula repetida
        if self.buscar_por_cedula(cedula) is not None:
            raise ValueError("Ya existe un visitante con esa cédula.")

        # Creamos el visitante y lo guardamos
        visitante = Visitante(cedula, nombre_completo, motivo_visita)
        self.__visitantes.append(visitante)

    # Devuelve una copia de la lista
    def obtener_visitantes(self):
        return self.__visitantes.copy()

    # Elimina un visitante según su cédula
    def eliminar_visitante(self, cedula):
        # Convertimos también a texto para comparar correctamente
        cedula = str(cedula).strip()

        visitante = self.buscar_por_cedula(cedula)

        if visitante is None:
            raise ValueError("No se encontró el visitante seleccionado.")

        self.__visitantes.remove(visitante)

    # Busca un visitante por cédula
    def buscar_por_cedula(self, cedula):
        # Convertimos a texto para evitar errores de comparación
        cedula = str(cedula).strip()

        for visitante in self.__visitantes:
            if str(visitante.cedula).strip() == cedula:
                return visitante

        return None