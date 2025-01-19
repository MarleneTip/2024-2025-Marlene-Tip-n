# Clase base Vehículo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.__año = año  # Atributo encapsulado (privado)

    # Método para acceder a la información del año (encapsulación)
    def obtener_año(self):
        return self.__año

    # Método común para todos los vehículos
    def arrancar(self):
        return f"{self.marca} {self.modelo} ha arrancado."

    # Método para obtener detalles del vehículo
    def detalles(self):
        return f"{self.marca} {self.modelo}, Año: {self.obtener_año()}"

# Clase derivada (Hija) - Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_combustible):
        super().__init__(marca, modelo, año)  # Llamada al constructor de la clase base
        self.tipo_combustible = tipo_combustible  # Atributo adicional específico para Coche

    # Sobreescritura de método (polimorfismo) de la clase base
    def arrancar(self):
        return f"El coche {self.marca} {self.modelo} con motor a {self.tipo_combustible} ha arrancado."

    # Método adicional para mostrar el tipo de combustible
    def mostrar_combustible(self):
        return f"Este coche utiliza {self.tipo_combustible}."

# Clase derivada (Hija) - Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)  # Llamada al constructor de la clase base
        self.tipo = tipo  # Atributo específico para Moto

    # Sobreescritura de método (polimorfismo) de la clase base
    def arrancar(self):
        return f"La moto {self.marca} {self.modelo} de tipo {self.tipo} ha arrancado."

    # Método adicional para mostrar el tipo de moto
    def mostrar_tipo(self):
        return f"Este es una moto de tipo {self.tipo}."

# Instanciamos objetos de las clases hijas
coche1 = Coche("Toyota", "Corolla", 2020, "gasolina")
moto1 = Moto("Yamaha", "R1", 2022, "deportiva")

# Demostración de polimorfismo
print(coche1.arrancar())  # Salida: El coche Toyota Corolla con motor a gasolina ha arrancado.
print(moto1.arrancar())   # Salida: La moto Yamaha R1 de tipo deportiva ha arrancado.

# Mostrar detalles adicionales de los vehículos
print(coche1.mostrar_combustible())  # Salida: Este coche utiliza gasolina.
print(moto1.mostrar_tipo())          # Salida: Este es una moto de tipo deportiva.

# Acceso al atributo encapsulado
print(f"El año de fabricación del coche es: {coche1.obtener_año()}")  # Salida: El año de fabricación del coche es: 2020
