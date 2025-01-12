# Definir una clase llamada Reserva
class Reserva:
    def __init__(self, cliente, fecha, numero_de_personas):
        self.cliente = cliente  # Atributo para almacenar el nombre del cliente
        self.fecha = fecha      # Atributo para almacenar la fecha de la reserva
        self.numero_de_personas = numero_de_personas  # Atributo para el número de personas

    def mostrar_reserva(self):
        # Método para mostrar la información de la reserva
        print(f"Reserva para {self.cliente} en la fecha {self.fecha} para {self.numero_de_personas} personas.")

    def modificar_reserva(self, nueva_fecha, nuevo_numero_de_personas):
        # Método para modificar una reserva
        self.fecha = nueva_fecha
        self.numero_de_personas = nuevo_numero_de_personas
        print("Reserva modificada exitosamente.")


# Crear objetos de la clase Reserva
reserva1 = Reserva("Juan Pérez", "2025-02-10", 4)
reserva2 = Reserva("María García", "2025-02-15", 2)

# Mostrar las reservas
reserva1.mostrar_reserva()
reserva2.mostrar_reserva()

# Modificar una reserva
reserva1.modificar_reserva("2025-02-12", 6)
reserva1.mostrar_reserva()
