# Clase que representa la información diaria del clima
class Clima:
    def __init__(self):
        self.temperaturas = []  # Atributo para almacenar las temperaturas de la semana

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        for i in range(7):  # 7 días de la semana
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        promedio = sum(self.temperaturas) / len(self.temperaturas)
        return promedio


# Función principal
def main():
    # Creamos una instancia de la clase Clima
    clima = Clima()

    # Ingresamos las temperaturas utilizando el método de la clase
    clima.ingresar_temperaturas()

    # Calculamos el promedio semanal utilizando el método de la clase
    promedio_semanal = clima.calcular_promedio()

    # Mostramos el resultado
    print(f"El promedio semanal de las temperaturas es: {promedio_semanal:.2f}°C")


# Llamamos a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
