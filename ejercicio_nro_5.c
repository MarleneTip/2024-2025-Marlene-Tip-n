#include <stdio.h>

int main() {
    int numeros[10];

    // Llenar el arreglo con números del 1 al 10
    for (int i = 0; i < 10; i++) {
        numeros[i] = i + 1;
    }

    // Mostrar los números en orden inverso separados por comas
    printf("Números del 10 al 1: ");
    for (int i = 9; i >= 0; i--) {
        printf("%d", numeros[i]);
        if (i > 0) {
            printf(", ");
        }
    }
    printf("\n");

    return 0;
}
