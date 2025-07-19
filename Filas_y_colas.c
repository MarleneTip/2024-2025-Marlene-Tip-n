#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 30  // Máximo número de personas/asientos

// Estructura para una persona (solo el nombre)
typedef struct {
    char nombre[50];  // Nombre de la persona (hasta 49 caracteres)
} Persona;

// Estructura de la cola
typedef struct {
    Persona cola[MAX];  // Arreglo que almacena hasta 30 personas
    int frente;
    int final;
    int cantidad;
} Cola;

// Inicializa la cola vacía
void inicializarCola(Cola *c) {
    c->frente = 0;
    c->final = -1;
    c->cantidad = 0;
}

// Verifica si la cola está llena (ya hay 30 personas)
int colaLlena(Cola *c) {
    return c->cantidad == MAX;
}

// Verifica si la cola está vacía
int colaVacia(Cola *c) {
    return c->cantidad == 0;
}

// Agrega una persona a la cola
void encolar(Cola *c) {
    if (colaLlena(c)) {
        printf("\n⚠️  Ya no hay asientos disponibles. La cola está llena.\n");
        return;
    }

    Persona p;
    printf("Ingrese el nombre de la persona: ");
    scanf(" %[^\n]", p.nombre);  // Lee nombre con espacios

    c->final = (c->final + 1) % MAX;
    c->cola[c->final] = p;
    c->cantidad++;

    printf("✅ Persona agregada con éxito.\n");
}

// Muestra las personas que están en la cola
void mostrarCola(Cola *c) {
    if (colaVacia(c)) {
        printf("\n🚫 No hay personas en la cola.\n");
        return;
    }

    printf("\n👥 Personas en espera (orden de llegada):\n");
    for (int i = 0; i < c->cantidad; i++) {
        int index = (c->frente + i) % MAX;
        printf(" - %s\n", c->cola[index].nombre);
    }
}

// Asigna asientos y vacía la cola
void asignarAsientos(Cola *c) {
    if (colaVacia(c)) {
        printf("\n🚫 No hay personas para asignar asientos.\n");
        return;
    }

    printf("\n🎢 Asignación de asientos:\n");
    int asiento = 1;
    while (!colaVacia(c)) {
        Persona p = c->cola[c->frente];
        printf(" - Asiento #%d: %s\n", asiento++, p.nombre);
        c->frente = (c->frente + 1) % MAX;
        c->cantidad--;
    }

    printf("✅ Todos los asientos han sido asignados. ¡Disfruten la atracción!\n");
}

// Menú principal
int main() {
    Cola cola;
    inicializarCola(&cola);
    int opcion;

    do {
        printf("\n--- MENÚ DE LA ATRACCIÓN ---\n");
        printf("1. Agregar persona a la cola\n");
        printf("2. Mostrar personas en espera\n");
        printf("3. Asignar asientos y abordar\n");
        printf("4. Salir\n");
        printf("Seleccione una opción: ");
        scanf("%d", &opcion);

        switch (opcion) {
            case 1:
                encolar(&cola);
                break;
            case 2:
                mostrarCola(&cola);
                break;
            case 3:
                asignarAsientos(&cola);
                break;
            case 4:
                printf("\n👋 Gracias por usar el sistema de la atracción.\n");
                break;
            default:
                printf("❌ Opción no válida. Intente de nuevo.\n");
        }
    } while (opcion != 4);

    return 0;
}
