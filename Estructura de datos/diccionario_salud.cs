using System;
using System.Collections.Generic;

namespace TraductorBasico
{
    class Program
    {
        static void Main(string[] args)
        {
            // Diccionario de síntomas: palabra clave en español → palabra en inglés
            Dictionary<string, string> diccionario = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase)
            {
                {"cabeza", "head"},
                {"estomago", "stomach"},
                {"fiebre", "fever"},
                {"tos", "cough"},
                {"resfriado", "cold"},
                {"garganta", "throat"},
                {"nausea", "nausea"},
                {"mareo", "dizziness"},
                {"fatiga", "fatigue"},
                {"diarrea", "diarrhea"}
            };

            int opcion = -1;

            while (opcion != 0)
            {
                Console.WriteLine("\n==================== MENÚ ====================");
                Console.WriteLine("1. Traducir una frase");
                Console.WriteLine("2. Agregar palabras al diccionario");
                Console.WriteLine("0. Salir");
                Console.Write("Seleccione una opción: ");

                if (!int.TryParse(Console.ReadLine(), out opcion))
                {
                    Console.WriteLine("⚠️ Opción no válida, intente de nuevo.");
                    continue;
                }

                switch (opcion)
                {
                    case 1:
                        TraducirFrase(diccionario);
                        break;
                    case 2:
                        AgregarPalabra(diccionario);
                        break;
                    case 0:
                        Console.WriteLine("👋 Saliendo del programa...");
                        break;
                    default:
                        Console.WriteLine("⚠️ Opción no válida, intente de nuevo.");
                        break;
                }
            }
        }

        // Traducir frase palabra por palabra usando el diccionario
        static void TraducirFrase(Dictionary<string, string> diccionario)
        {
            Console.Write("\nIngrese una frase en español: ");
            string frase = Console.ReadLine();

            // Separar frase en palabras
            string[] palabras = frase.Split(' ');

            for (int i = 0; i < palabras.Length; i++)
            {
                string palabraLimpia = palabras[i].Trim(new char[] { '.', ',', ';', '!', '?' }).ToLower();

                if (diccionario.ContainsKey(palabraLimpia))
                {
                    // Mantener la puntuación original
                    string puntuacion = "";
                    if (palabras[i].EndsWith(".") || palabras[i].EndsWith(",") ||
                        palabras[i].EndsWith(";") || palabras[i].EndsWith("!") || palabras[i].EndsWith("?"))
                    {
                        puntuacion = palabras[i].Substring(palabras[i].Length - 1);
                    }

                    palabras[i] = diccionario[palabraLimpia] + puntuacion;
                }
            }

            Console.WriteLine("\n🔎 Traducción: ");
            Console.WriteLine(string.Join(" ", palabras));
        }

        // Agregar nueva palabra clave al diccionario
        static void AgregarPalabra(Dictionary<string, string> diccionario)
        {
            Console.Write("\nIngrese la palabra en español: ");
            string espanol = Console.ReadLine().ToLower();

            Console.Write("Ingrese la traducción al inglés: ");
            string ingles = Console.ReadLine();

            if (!diccionario.ContainsKey(espanol))
            {
                diccionario.Add(espanol, ingles);
                Console.WriteLine($"✅ Se agregó: {espanol} → {ingles}");
            }
            else
            {
                Console.WriteLine("⚠️ Esa palabra ya existe en el diccionario.");
            }
        }
    }
}
