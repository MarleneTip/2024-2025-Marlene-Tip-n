#include <stdio.h>

int main() {
    char asignaturas[5][20] = {
        "Matematicas",
        "Fisica",
        "Quimica",
        "Historia",
        "Lengua"
    };

    // Mostrar el mensaje para cada asignatura
    for (int i = 0; i < 5; i++) {
        printf("Yo estudio %s\n", asignaturas[i]);
    }

    return 0;
}
