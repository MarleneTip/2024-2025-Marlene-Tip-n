#include <stdio.h>
#define PI 3.1416

// ----------------------
// Estructura para Círculo
// ----------------------
typedef struct {
    float radio;
} Circulo;

// Función para calcular el área del círculo
float areaCirculo(Circulo c) {
    return PI * c.radio * c.radio;
}

// Función para calcular el perímetro del círculo
float perimetroCirculo(Circulo c) {
    return 2 * PI * c.radio;
}

// ------------------------
// Estructura para Rectángulo
// ------------------------
typedef struct {
    float base;
    float altura;
} Rectangulo;

// Función para calcular el área del rectángulo
float areaRectangulo(Rectangulo r) {
    return r.base * r.altura;
}

// Función para calcular el perímetro del rectángulo
float perimetroRectangulo(Rectangulo r) {
    return 2 * (r.base + r.altura);
}

// -------------------------
// Función principal (main)
// -------------------------
int main() {
    Circulo miCirculo;
    miCirculo.radio = 5.0;

    Rectangulo miRectangulo;
    miRectangulo.base = 4.0;
    miRectangulo.altura = 6.0;

    printf("Círculo:\n");
    printf("Área: %.2f\n", areaCirculo(miCirculo));
    printf("Perímetro: %.2f\n", perimetroCirculo(miCirculo));

    printf("\nRectángulo:\n");
    printf("Área: %.2f\n", areaRectangulo(miRectangulo));
    printf("Perímetro: %.2f\n", perimetroRectangulo(miRectangulo));

    return 0;
}
