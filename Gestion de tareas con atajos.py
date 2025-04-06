import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Campo de entrada
        self.entry = tk.Entry(root, font=('Arial', 14))
        self.entry.pack(pady=10)
        self.entry.focus()

        # Botones
        button_frame = tk.Frame(root)
        button_frame.pack()

        self.add_button = tk.Button(button_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(button_frame, text="Marcar Completada", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, font=('Arial', 14), selectmode=tk.SINGLE)
        self.task_listbox.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Mapeo de tareas (índice → estado)
        self.task_states = {}

        # Atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<C>', lambda event: self.complete_task())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<D>', lambda event: self.delete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            index = self.task_listbox.size()
            self.task_listbox.insert(tk.END, task)
            self.task_states[index] = False  # False = pendiente
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "Por favor escribe una tarea.")

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task_text = self.task_listbox.get(index)
            if not self.task_states.get(index, False):
                # Marcar como completada
                self.task_listbox.delete(index)
                completed_task = f"✔️ {task_text}"
                self.task_listbox.insert(index, completed_task)
                self.task_states[index] = True
            else:
                # Ya está completada, desmarcar
                raw_task = task_text.replace("✔️ ", "")
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, raw_task)
                self.task_states[index] = False

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.task_listbox.delete(index)
            del self.task_states[index]
            # Reindexar estados de tarea
            self.task_states = {i: self.task_states.get(i + 1, False) for i in range(self.task_listbox.size())}

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
