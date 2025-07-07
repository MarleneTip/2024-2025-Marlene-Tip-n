#include <stdio.h>
#include <stdlib.h>

// Definimos la estructura de un nodo de la lista
struct Nodo {
    int dato;                    // Dato que almacena el nodo
    struct Nodo* siguiente;      // Puntero al siguiente nodo
};

// Función que cuenta los elementos de una lista enlazada
int contarElementos(struct Nodo* cabeza) {
    int contador = 0;               // Contador inicializado en 0
    struct Nodo* actual = cabeza;   // Puntero auxiliar para recorrer la lista

    // Recorremos la lista hasta que lleguemos al final (NULL)
    while (actual != NULL) {
        contador++;                 // Contamos este nodo
        actual = actual->siguiente; // Avanzamos al siguiente nodo
    }

    return contador;  // Retornamos el total contado
}

int main() {
    // Creamos manualmente tres nodos usando malloc (memoria dinámica)
    struct Nodo* nodo1 = (struct Nodo*) malloc(sizeof(struct Nodo));
    struct Nodo* nodo2 = (struct Nodo*) malloc(sizeof(struct Nodo));
    struct Nodo* nodo3 = (struct Nodo*) malloc(sizeof(struct Nodo));

    // Asignamos valores a los nodos
    nodo1->dato = 5;
    nodo2->dato = 10;
    nodo3->dato = 15;

    // Enlazamos los nodos uno tras otro
    nodo1->siguiente = nodo2;
    nodo2->siguiente = nodo3;
    nodo3->siguiente = NULL;  // El último nodo apunta a NULL

    // 'nodo1' es el primer nodo, es decir, la cabeza de la lista
    struct Nodo* cabeza = nodo1;

    // Llamamos a la función que cuenta los elementos de la lista
    int total = contarElementos(cabeza);

    // Mostramos el resultado por pantalla
    printf("La lista tiene %d elementos.\n", total);

    // Liberamos la memoria reservada con malloc
    free(nodo1);
    free(nodo2);
    free(nodo3);

    return 0;
}
