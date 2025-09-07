#include <stdio.h>
#include <string.h>

#define MAX_EQUIPOS 3
#define MAX_JUGADORES 10
#define MAX_NOMBRE 50

// Estructura para almacenar un equipo y sus jugadores
typedef struct {
    char nombre_equipo[MAX_NOMBRE];
    char jugadores[MAX_JUGADORES][MAX_NOMBRE];
    int num_jugadores;
} Equipo;

// Función para verificar si un jugador ya existe en un arreglo
int jugadorRepetido(char jugador[], char lista[][MAX_NOMBRE], int n) {
    for (int i = 0; i < n; i++) {
        if (strcmp(jugador, lista[i]) == 0)
            return 1; // Sí está repetido
    }
    return 0; // No está repetido
}

int main() {
    // ========================================================
    // Paso 1: Crear equipos y jugadores
    // ========================================================
    Equipo equipos[MAX_EQUIPOS] = {
        {"Equipo A", {"Juan", "Pedro", "Luis"}, 3},
        {"Equipo B", {"Carlos", "Ana", "Luis"}, 3},
        {"Equipo C", {"Miguel", "Pedro", "Sofia"}, 3}
    };

    // ========================================================
    // Paso 2: Reportería - Mostrar todos los equipos y jugadores
    // ========================================================
    printf("Listado de equipos y jugadores:\n");
    for (int i = 0; i < MAX_EQUIPOS; i++) {
        printf("%s: ", equipos[i].nombre_equipo);
        for (int j = 0; j < equipos[i].num_jugadores; j++) {
            printf("%s ", equipos[i].jugadores[j]);
        }
        printf("\n");
    }

    // ========================================================
    // Paso 3: Detectar jugadores que participan en más de un equipo
    // ========================================================
    char jugadores_todos[MAX_EQUIPOS * MAX_JUGADORES][MAX_NOMBRE];
    char jugadores_repetidos[MAX_EQUIPOS * MAX_JUGADORES][MAX_NOMBRE];
    int total = 0;
    int repetidos = 0;

    for (int i = 0; i < MAX_EQUIPOS; i++) {
        for (int j = 0; j < equipos[i].num_jugadores; j++) {
            if (jugadorRepetido(equipos[i].jugadores[j], jugadores_todos, total)) {
                // Si ya estaba, es repetido
                if (!jugadorRepetido(equipos[i].jugadores[j], jugadores_repetidos, repetidos)) {
                    strcpy(jugadores_repetidos[repetidos], equipos[i].jugadores[j]);
                    repetidos++;
                }
            } else {
                strcpy(jugadores_todos[total], equipos[i].jugadores[j]);
                total++;
            }
        }
    }

    printf("\nJugadores que participan en más de un equipo:\n");
    for (int i = 0; i < repetidos; i++) {
        printf("%s ", jugadores_repetidos[i]);
    }
    printf("\n");

    // ========================================================
    // Paso 4: Consultar jugadores de un equipo específico
    // ========================================================
    char equipo_consulta[MAX_NOMBRE] = "Equipo B";
    printf("\nJugadores en %s: ", equipo_consulta);
    for (int i = 0; i < MAX_EQUIPOS; i++) {
        if (strcmp(equipos[i].nombre_equipo, equipo_consulta) == 0) {
            for (int j = 0; j < equipos[i].num_jugadores; j++) {
                printf("%s ", equipos[i].jugadores[j]);
            }
            break;
        }
    }
    printf("\n");

    return 0;
}
