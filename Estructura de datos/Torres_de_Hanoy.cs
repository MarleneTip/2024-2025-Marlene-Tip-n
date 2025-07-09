using System;
using System.Collections.Generic;

class TorresDeHanoiConPilas
{
    // Declaramos tres pilas para representar las torres A, B y C
    static Stack<int> torreA = new Stack<int>();
    static Stack<int> torreB = new Stack<int>();
    static Stack<int> torreC = new Stack<int>();

    static void Main()
    {
        int n; // Número de discos

        // Solicitamos al usuario cuántos discos quiere usar
        Console.Write("Ingrese el número de discos: ");
        n = int.Parse(Console.ReadLine());

        // Inicializamos la torre A con los discos, del más grande (n) al más pequeño (1)
        for (int i = n; i >= 1; i--)
        {
            torreA.Push(i); // Apilamos los discos en torreA
        }

        Console.WriteLine("\n--- Inicio del proceso ---\n");

        // Iniciamos la solución recursiva:
        // - Mover todos los discos desde torre A hasta torre C
        // - Usamos torre B como torre auxiliar
        ResolverHanoi(n, torreA, torreC, torreB, 'A', 'C', 'B');
    }

    /// <summary>
    /// Función recursiva para resolver el problema de las Torres de Hanoi
    /// </summary>
    /// <param name="n">Número de discos a mover</param>
    /// <param name="origen">Torre de origen</param>
    /// <param name="destino">Torre de destino</param>
    /// <param name="auxiliar">Torre auxiliar</param>
    /// <param name="nombreOrigen">Nombre de la torre origen (A, B, C)</param>
    /// <param name="nombreDestino">Nombre de la torre destino</param>
    /// <param name="nombreAuxiliar">Nombre de la torre auxiliar</param>
    static void ResolverHanoi(int n, Stack<int> origen, Stack<int> destino, Stack<int> auxiliar,
                              char nombreOrigen, char nombreDestino, char nombreAuxiliar)
    {
        if (n == 1)
        {
            // Caso base: mover un solo disco directamente del origen al destino
            MoverDisco(origen, destino, nombreOrigen, nombreDestino);
            return;
        }

        // Paso 1: mover n-1 discos del origen al auxiliar, usando el destino como ayuda
        ResolverHanoi(n - 1, origen, auxiliar, destino, nombreOrigen, nombreAuxiliar, nombreDestino);

        // Paso 2: mover el disco más grande restante directamente al destino
        MoverDisco(origen, destino, nombreOrigen, nombreDestino);

        // Paso 3: mover los n-1 discos del auxiliar al destino, usando el origen como ayuda
        ResolverHanoi(n - 1, auxiliar, destino, origen, nombreAuxiliar, nombreDestino, nombreOrigen);
    }

    /// <summary>
    /// Función que realiza el movimiento de un disco entre dos torres
    /// </summary>
    /// <param name="origen">Torre origen</param>
    /// <param name="destino">Torre destino</param>
    /// <param name="nombreOrigen">Nombre de la torre origen</param>
    /// <param name="nombreDestino">Nombre de la torre destino</param>
    static void MoverDisco(Stack<int> origen, Stack<int> destino, char nombreOrigen, char nombreDestino)
    {
        int disco = origen.Pop(); // Quitamos el disco superior de la torre de origen
        destino.Push(disco);      // Lo colocamos en la cima de la torre de destino

        // Mostramos el movimiento que se realizó
        Console.WriteLine($"Mover disco {disco} desde torre {nombreOrigen} hacia torre {nombreDestino}");
    }
}
