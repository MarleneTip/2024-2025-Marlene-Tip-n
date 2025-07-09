using System;
using System.Collections.Generic;

class ProgramaVerificacionBalanceo
{
    static void Main()
    {
        // Solicita al usuario que ingrese una expresión matemática
        Console.WriteLine("Ingrese la expresión matemática:");
        string expresion = Console.ReadLine();

        // Llama al método que verifica si la expresión está balanceada
        if (EstaBalanceada(expresion))
        {
            Console.WriteLine("Fórmula balanceada.");
        }
        else
        {
            Console.WriteLine("Fórmula NO balanceada.");
        }
    }

    // Método para verificar si los paréntesis, llaves y corchetes están balanceados
    static bool EstaBalanceada(string expresion)
    {
        // Se utiliza una pila para almacenar los símbolos de apertura
        Stack<char> pila = new Stack<char>();

        // Recorremos cada carácter en la expresión ingresada
        foreach (char caracter in expresion)
        {
            // Si el carácter es un símbolo de apertura, se apila
            if (caracter == '(' || caracter == '{' || caracter == '[')
            {
                pila.Push(caracter);
            }
            // Si el carácter es un símbolo de cierre
            else if (caracter == ')' || caracter == '}' || caracter == ']')
            {
                // Si la pila está vacía, hay un cierre sin apertura previa -> no balanceado
                if (pila.Count == 0)
                    return false;

                // Sacamos el último símbolo de apertura de la pila
                char simboloApertura = pila.Pop();

                // Verificamos si el símbolo de apertura y el de cierre coinciden
                if (!EsPar(simboloApertura, caracter))
                    return false; // Si no coinciden, la expresión no está balanceada
            }

            // Otros caracteres (números, signos, espacios) se ignoran
        }

        // Si al final la pila está vacía, todos los símbolos fueron correctamente cerrados
        return pila.Count == 0;
    }

    // Método auxiliar que determina si el símbolo de apertura y cierre hacen pareja
    static bool EsPar(char apertura, char cierre)
    {
        return (apertura == '(' && cierre == ')') ||
               (apertura == '{' && cierre == '}') ||
               (apertura == '[' && cierre == ']');
    }
}
