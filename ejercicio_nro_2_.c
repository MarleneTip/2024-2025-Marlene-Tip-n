#include <stdio.h>

int main() {
    char asignaturas[5][20] = {
        "Matematicas",
        "Fisica",
        "Quimica",
        "Historia",
        "Lengua"
    };

    for (int i = 0; i < 5; i++) {
        printf("Yo estudio %s\n", asignaturas[i]);
    }

    return 0;
}
