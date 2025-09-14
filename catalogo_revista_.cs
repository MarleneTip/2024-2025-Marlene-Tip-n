using System;
using System.Collections.Generic;

namespace CatalogoRevistasMedicas
{
    class Program
    {
        // Lista dinámica que almacena los títulos de revistas médicas
        static List<string> catalogo = new List<string>()
        {
            "The New England Journal of Medicine",
            "The Lancet",
            "JAMA (Journal of the American Medical Association)",
            "BMJ (British Medical Journal)",
            "Annals of Internal Medicine",
            "Nature Medicine",
            "Pediatrics",
            "Neurology",
            "Circulation",
            "European Heart Journal"
        };

        static void Main(string[] args)
        {
            int opcion;
            // Menú principal: repetir hasta que el usuario elija salir
            do
            {
                Console.Clear();
                Console.WriteLine("=== Catálogo de Revistas Médicas ===");
                Console.WriteLine("1. Buscar título");
                Console.WriteLine("2. Mostrar todos");
                Console.WriteLine("3. Salir");
                Console.Write("Seleccione una opción: ");

                if (!int.TryParse(Console.ReadLine(), out opcion)) opcion = 0;

                switch (opcion)
                {
                    case 1:
                        Console.Write("\nIngrese el título a buscar: ");
                        string titulo = (Console.ReadLine() ?? "").Trim();
                        bool encontrado = BuscarRecursivo(catalogo, titulo, 0);
                        Console.WriteLine(encontrado ? "\nEncontrado" : "\nNo encontrado");
                        Console.ReadKey();
                        break;

                    case 2:
                        Console.WriteLine("\nCatálogo completo:");
                        foreach (var revista in catalogo) Console.WriteLine("- " + revista);
                        Console.ReadKey();
                        break;

                    case 3:
                        Console.WriteLine("\nSaliendo...");
                        break;

                    default:
                        Console.WriteLine("\nOpción inválida");
                        Console.ReadKey();
                        break;
                }
            } while (opcion != 3);
        }

        // Búsqueda recursiva: recorre la lista comparando títulos sin importar mayúsculas
        static bool BuscarRecursivo(List<string> lista, string titulo, int indice)
        {
            if (indice >= lista.Count) return false;
            if (lista[indice].Equals(titulo, StringComparison.OrdinalIgnoreCase)) return true;
            return BuscarRecursivo(lista, titulo, indice + 1);
        }
    }
}
