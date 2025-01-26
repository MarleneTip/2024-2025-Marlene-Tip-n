class Documento:
    def __init__(self, nombre, contenido):
        """
        Constructor de la clase Documento. Inicializa el nombre y el contenido
        del documento cuando se crea una nueva instancia de esta clase.

        :param nombre: Nombre del documento.
        :param contenido: Contenido del documento.
        """
        self.nombre = nombre
        self.contenido = contenido
        print(f"Documento '{self.nombre}' creado.")

    def __del__(self):
        """
        Destructor de la clase Documento. Este método se llama cuando el objeto
        es destruido (por ejemplo, cuando se elimina o se sale del ámbito).
        Aquí podemos realizar tareas de limpieza, como cerrar archivos abiertos
        o liberar recursos.
        """
        print(f"Documento '{self.nombre}' destruido.")

    def mostrar_documento(self):
        """
        Muestra el contenido del documento en la consola.
        """
        print(f"Contenido de '{self.nombre}':\n{self.contenido}")


# Crear una instancia de la clase Documento
doc = Documento("Ejemplo1", "Este es un documento de prueba.")
doc.mostrar_documento()

# Eliminar la referencia al objeto
del doc

# Ahora el objeto será destruido y el destructor será llamado automáticamente
