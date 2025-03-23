import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
import os
import csv

# Nombre del archivo para almacenar los eventos
archivo_eventos = "eventos.csv"


# Función para cargar los eventos desde el archivo
def cargar_eventos():
    if os.path.exists(archivo_eventos):
        with open(archivo_eventos, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                eventos_tree.insert("", "end", values=row)


# Función para guardar los eventos en el archivo
def guardar_eventos():
    with open(archivo_eventos, mode='w', newline='') as file:
        writer = csv.writer(file)
        for item in eventos_tree.get_children():
            writer.writerow(eventos_tree.item(item)["values"])


# Función para agregar un evento a la lista
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        # Agregar el evento a la Treeview
        eventos_tree.insert("", "end", values=(fecha, hora, descripcion))
        guardar_eventos()  # Guardar los eventos después de agregar
        # Limpiar los campos de entrada
        entry_fecha.delete(0, "end")
        entry_hora.delete(0, "end")
        entry_descripcion.delete(0, "end")
    else:
        messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")


# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccionado = eventos_tree.selection()
    if seleccionado:
        respuesta = messagebox.askyesno("Eliminar Evento", "¿Estás seguro de que deseas eliminar este evento?")
        if respuesta:
            eventos_tree.delete(seleccionado)
            guardar_eventos()  # Guardar los eventos después de eliminar
    else:
        messagebox.showwarning("No Seleccionado", "Por favor, selecciona un evento para eliminar.")


# Función para seleccionar la fecha desde el calendario
def seleccionar_fecha_calendario():
    entry_fecha.delete(0, "end")
    entry_fecha.insert(0, calendario.get_date())


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")

# Crear un Frame para la lista de eventos
frame_lista_eventos = tk.Frame(ventana)
frame_lista_eventos.pack(padx=10, pady=10)

# Crear la lista de eventos (Treeview)
eventos_tree = ttk.Treeview(frame_lista_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings")
eventos_tree.heading("Fecha", text="Fecha")
eventos_tree.heading("Hora", text="Hora")
eventos_tree.heading("Descripción", text="Descripción")
eventos_tree.pack()

# Crear un Frame para los campos de entrada
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(padx=10, pady=10)

# Etiqueta y campo de entrada para la fecha
label_fecha = tk.Label(frame_entrada, text="Fecha (DD/MM/YYYY):")
label_fecha.grid(row=0, column=0)
entry_fecha = tk.Entry(frame_entrada)
entry_fecha.grid(row=0, column=1)

# Etiqueta y campo de entrada para la hora
label_hora = tk.Label(frame_entrada, text="Hora (HH:MM):")
label_hora.grid(row=1, column=0)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1)

# Etiqueta y campo de entrada para la descripción
label_descripcion = tk.Label(frame_entrada, text="Descripción:")
label_descripcion.grid(row=2, column=0)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1)

# Crear un Frame para los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(padx=10, pady=10)

# Botón para agregar un evento
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5)

# Botón para eliminar un evento seleccionado
btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5)

# Botón para salir de la aplicación
btn_salir = tk.Button(frame_botones, text="Salir", command=ventana.quit)
btn_salir.grid(row=0, column=2, padx=5)

# Implementar el DatePicker utilizando un widget adicional (tkcalendar)
calendario = Calendar(ventana, selectmode='day', date_pattern='dd/mm/yyyy')
calendario.pack(padx=10, pady=10)

# Botón para seleccionar la fecha desde el calendario
btn_seleccionar_fecha = tk.Button(ventana, text="Seleccionar Fecha desde Calendario",
                                  command=seleccionar_fecha_calendario)
btn_seleccionar_fecha.pack(padx=10, pady=10)

# Cargar los eventos almacenados al iniciar la aplicación
cargar_eventos()

# Iniciar la aplicación
ventana.mainloop()
