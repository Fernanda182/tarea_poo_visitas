# Importamos tkinter
import tkinter as tk

# Importamos la clase de servicio
from servicios.visita_servicio import VisitaServicio

# Importamos la interfaz gráfica
from ui.app_tkinter import AppTkinter


# Función principal
def main():
    # Creamos la ventana principal
    root = tk.Tk()

    # Creamos el servicio
    servicio = VisitaServicio()

    # Inyectamos el servicio en la interfaz
    app = AppTkinter(root, servicio)

    # Iniciamos el ciclo principal de la ventana
    root.mainloop()


# Punto de entrada del programa
if __name__ == "__main__":
    main()