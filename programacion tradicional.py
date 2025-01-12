# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # 7 días de la semana
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio


# Función principal
def main():
    # Ingresamos las temperaturas
    temperaturas = ingresar_temperaturas()

    # Calculamos el promedio semanal
    promedio_semanal = calcular_promedio(temperaturas)

    # Mostramos el resultado
    print(f"El promedio semanal de las temperaturas es: {promedio_semanal:.2f}°C")


# Llamamos a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
