import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

def mark_completed():
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)
        task_listbox.delete(selected_index)
        task_listbox.insert(selected_index, "✔ " + task)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def on_enter(event):
    add_task()

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Campo de entrada y botones
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
task_entry.bind("<Return>", on_enter)  # Permitir añadir con Enter

add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack()

complete_button = tk.Button(root, text="Marcar como Completada", command=mark_completed)
complete_button.pack()

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack()

# Listbox para mostrar las tareas
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

root.mainloop()
