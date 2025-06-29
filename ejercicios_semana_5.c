#include <stdio.h>

int main() {
    // Arreglo de cadenas: 5 asignaturas, cada una con hasta 20 caracteres
    char asignaturas[5][20] = {
        "Matematicas",
        "Fisica",
        "Quimica",
        "Historia",
        "Lengua"
    };

    // Mostrar las asignaturas
    printf("Asignaturas del curso:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d. %s\n", i + 1, asignaturas[i]);
    }

    return 0;
}
