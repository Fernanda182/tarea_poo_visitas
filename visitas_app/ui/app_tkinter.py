# Importamos tkinter para crear la interfaz gráfica
import tkinter as tk

# Importamos componentes adicionales de tkinter
from tkinter import ttk, messagebox


# Clase de la interfaz gráfica
# Recibe el servicio como parámetro (inyección de dependencias)
class AppTkinter:
    def __init__(self, root, servicio):
        # Ventana principal
        self.root = root

        # Servicio que contiene la lógica del sistema
        self.servicio = servicio

        # Configuración de la ventana
        self.root.title("Sistema de Registro de Visitantes")
        self.root.geometry("760x500")
        self.root.resizable(False, False)

        # Llamamos al método que crea todos los componentes visuales
        self.crear_widgets()

        # Cargamos la tabla inicialmente vacía
        self.actualizar_tabla()

    # Método para construir toda la interfaz
    def crear_widgets(self):
        # =========================
        # TÍTULO PRINCIPAL
        # =========================
        titulo = tk.Label(
            self.root,
            text="Sistema de Registro de Visitantes",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)

        # =========================
        # FORMULARIO DE ENTRADA
        # =========================
        frame_formulario = tk.Frame(self.root)
        frame_formulario.pack(pady=10)

        # Etiqueta y caja de texto para cédula
        lbl_cedula = tk.Label(frame_formulario, text="Cédula:")
        lbl_cedula.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        self.entry_cedula = tk.Entry(frame_formulario, width=35)
        self.entry_cedula.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y caja de texto para nombre completo
        lbl_nombre = tk.Label(frame_formulario, text="Nombre completo:")
        lbl_nombre.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.entry_nombre = tk.Entry(frame_formulario, width=35)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=5)

        # Etiqueta y caja de texto para motivo de visita
        lbl_motivo = tk.Label(frame_formulario, text="Motivo de la visita:")
        lbl_motivo.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.entry_motivo = tk.Entry(frame_formulario, width=35)
        self.entry_motivo.grid(row=2, column=1, padx=10, pady=5)

        # =========================
        # BOTONES DE ACCIÓN
        # =========================
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        # Botón para registrar visitante
        btn_registrar = tk.Button(
            frame_botones,
            text="Registrar",
            width=15,
            command=self.registrar_visitante
        )
        btn_registrar.grid(row=0, column=0, padx=10)

        # Botón para eliminar visitante seleccionado
        btn_eliminar = tk.Button(
            frame_botones,
            text="Eliminar",
            width=15,
            command=self.eliminar_visitante
        )
        btn_eliminar.grid(row=0, column=1, padx=10)

        # Botón para limpiar los campos del formulario
        btn_limpiar = tk.Button(
            frame_botones,
            text="Limpiar Campos",
            width=15,
            command=self.limpiar_campos
        )
        btn_limpiar.grid(row=0, column=2, padx=10)

        # =========================
        # TABLA DE DATOS
        # =========================
        frame_tabla = tk.Frame(self.root)
        frame_tabla.pack(pady=20, fill="both", expand=True)

        # Definimos las columnas de la tabla
        columnas = ("cedula", "nombre", "motivo")

        # Creamos el Treeview
        self.tree = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            height=10
        )

        # Configuramos los encabezados
        self.tree.heading("cedula", text="Cédula")
        self.tree.heading("nombre", text="Nombre Completo")
        self.tree.heading("motivo", text="Motivo de la Visita")

        # Configuramos el ancho y alineación de columnas
        self.tree.column("cedula", width=150, anchor="center")
        self.tree.column("nombre", width=250, anchor="center")
        self.tree.column("motivo", width=250, anchor="center")

        # Mostramos la tabla
        self.tree.pack(side="left", fill="both", expand=True)

        # Scroll vertical para la tabla
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    # Método que se ejecuta al pulsar el botón Registrar
    def registrar_visitante(self):
        # Obtenemos los valores escritos por el usuario
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        try:
            # Enviamos los datos al servicio para registrarlos
            self.servicio.registrar_visitante(cedula, nombre, motivo)

            # Mensaje de éxito
            messagebox.showinfo("Éxito", "Visitante registrado correctamente.")

            # Refrescamos la tabla
            self.actualizar_tabla()

            # Limpiamos el formulario
            self.limpiar_campos()

        except ValueError as e:
            # Mostramos advertencia si hubo error de validación
            messagebox.showwarning("Advertencia", str(e))

     # Método que se ejecuta al pulsar el botón Eliminar
    def eliminar_visitante(self):
        # Obtenemos la fila seleccionada en la tabla
        seleccion = self.tree.selection()

        # Si no se seleccionó nada, mostramos advertencia
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un visitante para eliminar.")
            return

        # Obtenemos la información de la fila seleccionada
        item = self.tree.item(seleccion[0])

        # Tomamos la cédula de la primera columna y la convertimos a texto
        cedula = str(item["values"][0]).strip()

        try:
            # Eliminamos el visitante usando la cédula seleccionada
            self.servicio.eliminar_visitante(cedula)

            # Mensaje de éxito
            messagebox.showinfo("Éxito", "Visitante eliminado correctamente.")

            # Actualizamos la tabla
            self.actualizar_tabla()

            # Limpiamos los campos
            self.limpiar_campos()

        except ValueError as e:
            messagebox.showwarning("Advertencia", str(e))
    # Método para borrar el contenido de los Entry
    def limpiar_campos(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)

    # Método para recargar la tabla con los datos actuales
    def actualizar_tabla(self):
        # Primero borramos todas las filas actuales
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        # Luego insertamos nuevamente todos los visitantes
        for visitante in self.servicio.obtener_visitantes():
            self.tree.insert(
                "",
                tk.END,
                values=(
                    visitante.cedula,
                    visitante.nombre_completo,
                    visitante.motivo_visita
                )
            )