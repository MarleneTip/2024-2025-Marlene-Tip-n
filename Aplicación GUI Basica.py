import tkinter as tk
from tkinter import messagebox


# Función para agregar un contacto a la lista
def agregar_contacto():
    # Obtener el nombre y número ingresados
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()

    # Validar que ambos campos no estén vacíos
    if nombre != "" and telefono != "":
        # Agregar el contacto a la lista
        lista_contactos.insert(tk.END, f"{nombre} - {telefono}")
        entry_nombre.delete(0, tk.END)  # Limpiar el campo de nombre
        entry_telefono.delete(0, tk.END)  # Limpiar el campo de teléfono
    else:
        # Mostrar advertencia si algún campo está vacío
        messagebox.showwarning("Advertencia", "Por favor, ingrese tanto el nombre como el número de teléfono.")


# Función para limpiar la lista de contactos
def limpiar_lista():
    lista_contactos.delete(0, tk.END)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Contactos")  # Título de la ventana
ventana.geometry("400x400")  # Tamaño de la ventana

# Etiqueta para el nombre
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_nombre.pack(pady=5)

# Campo de texto para el nombre
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.pack(pady=5)

# Etiqueta para el teléfono
etiqueta_telefono = tk.Label(ventana, text="Teléfono:")
etiqueta_telefono.pack(pady=5)

# Campo de texto para el teléfono
entry_telefono = tk.Entry(ventana, width=30)
entry_telefono.pack(pady=5)

# Botón para agregar el contacto
boton_agregar = tk.Button(ventana, text="Agregar Contacto", command=agregar_contacto)
boton_agregar.pack(pady=10)

# Lista para mostrar los contactos
lista_contactos = tk.Listbox(ventana, height=10, width=40)
lista_contactos.pack(pady=10)

# Botón para limpiar la lista de contactos
boton_limpiar = tk.Button(ventana, text="Limpiar Lista", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Ejecutar el ciclo principal de la interfaz gráfica
ventana.mainloop()
