#include <stdio.h>
#include <stdlib.h>

// Definición de la estructura Nodo
struct Nodo {
    int dato;               // Valor almacenado en el nodo
    struct Nodo* siguiente; // Puntero al siguiente nodo en la lista
};

// Función para imprimir todos los elementos de la lista
void imprimirLista(struct Nodo* cabeza) {
    struct Nodo* actual = cabeza;  // Empezamos desde la cabeza
    while (actual != NULL) {       // Mientras no lleguemos al final (NULL)
        printf("%d -> ", actual->dato); // Imprimimos el dato del nodo actual
        actual = actual->siguiente;      // Avanzamos al siguiente nodo
    }
    printf("NULL\n");  // Indicamos el fin de la lista
}

// Función para invertir una lista enlazada
struct Nodo* invertirLista(struct Nodo* cabeza) {
    struct Nodo* prev = NULL;    // Nodo previo, inicia en NULL porque el nuevo último apuntará a NULL
    struct Nodo* actual = cabeza; // Nodo actual que estamos procesando, empezamos en la cabeza
    struct Nodo* siguiente = NULL; // Nodo siguiente que guardaremos para no perder la referencia

    // Recorremos la lista hasta que actual sea NULL (fin de lista)
    while (actual != NULL) {
        siguiente = actual->siguiente; // Guardamos el siguiente nodo
        actual->siguiente = prev;      // Invertimos el enlace: actual apunta al nodo previo
        prev = actual;                 // Movemos prev al nodo actual
        actual = siguiente;            // Avanzamos actual al nodo siguiente
    }

    // Al terminar, prev es la nueva cabeza de la lista invertida
    return prev;
}

int main() {
    // Crear nodos en memoria dinámica
    struct Nodo* n1 = (struct Nodo*) malloc(sizeof(struct Nodo));
    struct Nodo* n2 = (struct Nodo*) malloc(sizeof(struct Nodo));
    struct Nodo* n3 = (struct Nodo*) malloc(sizeof(struct Nodo));
    struct Nodo* n4 = (struct Nodo*) malloc(sizeof(struct Nodo));

    // Asignar valores a cada nodo
    n1->dato = 10;
    n2->dato = 20;
    n3->dato = 30;
    n4->dato = 40;

    // Enlazar nodos para formar la lista: 10 -> 20 -> 30 -> 40 -> NULL
    n1->siguiente = n2;
    n2->siguiente = n3;
    n3->siguiente = n4;
    n4->siguiente = NULL; // Último nodo apunta a NULL

    // La cabeza de la lista es n1
    struct Nodo* cabeza = n1;

    printf("Lista original:\n");
    imprimirLista(cabeza);  // Mostramos la lista antes de invertirla

    // Invertimos la lista
    cabeza = invertirLista(cabeza);

    printf("Lista invertida:\n");
    imprimirLista(cabeza);  // Mostramos la lista después de invertirla

    // Liberar la memoria reservada para evitar fugas de memoria
    free(n1);
    free(n2);
    free(n3);
    free(n4);

    return 0;
}
