# Programa para calcular el área y el perímetro de figuras geométricas
# Este programa permite calcular el área y el perímetro de un cuadrado, un rectángulo y un círculo.
# El programa utiliza funciones y maneja diferentes tipos de datos: enteros, flotantes, cadenas y booleanos.

import math  # Importamos la librería math para el cálculo del área del círculo


# Función para calcular el área y el perímetro de un cuadrado
def calcular_cuadrado(lado):
    """Calcula el área y el perímetro de un cuadrado."""
    area = lado * lado  # Área = lado^2
    perimetro = 4 * lado  # Perímetro = 4 * lado
    return area, perimetro


# Función para calcular el área y el perímetro de un rectángulo
def calcular_rectangulo(base, altura):
    """Calcula el área y el perímetro de un rectángulo."""
    area = base * altura  # Área = base * altura
    perimetro = 2 * (base + altura)  # Perímetro = 2 * (base + altura)
    return area, perimetro


# Función para calcular el área y el perímetro de un círculo
def calcular_circulo(radio):
    """Calcula el área y el perímetro (circunferencia) de un círculo."""
    area = math.pi * radio * radio  # Área = pi * radio^2
    circunferencia = 2 * math.pi * radio  # Circunferencia = 2 * pi * radio
    return area, circunferencia


# Función principal para interactuar con el usuario
def main():
    """Solicita al usuario las dimensiones de la figura y muestra los resultados."""
    print("Seleccione una figura para calcular el área y el perímetro:")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Círculo")

    # Solicitar la opción de la figura
    figura = input("Ingrese el número de la figura (1, 2 o 3): ")

    # Verificar si la opción es válida
    if figura == "1":
        lado = float(input("Ingrese el valor del lado del cuadrado: "))  # Entrada de tipo float
        area, perimetro = calcular_cuadrado(lado)
        print(f"Área del cuadrado: {area} unidades cuadradas")
        print(f"Perímetro del cuadrado: {perimetro} unidades")
    elif figura == "2":
        base = float(input("Ingrese el valor de la base del rectángulo: "))
        altura = float(input("Ingrese el valor de la altura del rectángulo: "))
        area, perimetro = calcular_rectangulo(base, altura)
        print(f"Área del rectángulo: {area} unidades cuadradas")
        print(f"Perímetro del rectángulo: {perimetro} unidades")
    elif figura == "3":
        radio = float(input("Ingrese el valor del radio del círculo: "))
        area, circunferencia = calcular_circulo(radio)
        print(f"Área del círculo: {area} unidades cuadradas")
        print(f"Circunferencia del círculo: {circunferencia} unidades")
    else:
        print("Opción no válida. Por favor, ingrese 1, 2 o 3.")


# Ejecutar la función principal
if __name__ == "__main__":
    main()
