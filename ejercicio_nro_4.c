#include <stdio.h>

#define NUMEROS 6

void ordenar(int arr[], int n) {
    int temp;
    for (int i = 0; i < n -1; i++) {
        for (int j = i +1; j < n; j++) {
            if (arr[i] > arr[j]) {
                // Intercambio
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main() {
    int numeros[NUMEROS];

    // Pedir los números
    printf("Introduce los %d números ganadores de la lotería:\n", NUMEROS);
    for (int i = 0; i < NUMEROS; i++) {
        printf("Número %d: ", i + 1);
        scanf("%d", &numeros[i]);
    }

    // Ordenar los números
    ordenar(numeros, NUMEROS);

    // Mostrar números ordenados
    printf("\nNúmeros ganadores ordenados de menor a mayor:\n");
    for (int i = 0; i < NUMEROS; i++) {
        printf("%d ", numeros[i]);
    }
    printf("\n");

    return 0;
}
