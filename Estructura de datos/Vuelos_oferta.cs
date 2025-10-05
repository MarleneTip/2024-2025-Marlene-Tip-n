using System;
using System.Collections.Generic;

namespace VuelosEnPromocion
{
    class Program
    {
        // Clase para representar un vuelo
        class Vuelo
        {
            public string Origen { get; set; }
            public string Destino { get; set; }
            public double Precio { get; set; }

            public Vuelo(string origen, string destino, double precio)
            {
                Origen = origen;
                Destino = destino;
                Precio = precio;
            }

            public override string ToString()
            {
                return $"Origen: {Origen}, Destino: {Destino}, Precio: ${Precio}";
            }
        }

        static void Main(string[] args)
        {
            // Base de datos ficticia de vuelos en Latinoamérica
            List<Vuelo> vuelos = new List<Vuelo>
            {
                new Vuelo("Bogotá", "Lima", 250),
                new Vuelo("Buenos Aires", "Santiago", 200),
                new Vuelo("Ciudad de México", "Guatemala", 180),
                new Vuelo("Quito", "Lima", 150),
                new Vuelo("Sao Paulo", "Buenos Aires", 220),
                new Vuelo("Caracas", "Bogotá", 210),
                new Vuelo("Lima", "Santiago", 170),
                new Vuelo("Montevideo", "Buenos Aires", 160)
            };

            bool salir = false;

            while (!salir)
            {
                Console.Clear();
                Console.WriteLine("=== VUELOS EN PROMOCIÓN ===");
                Console.WriteLine("1. Mostrar todos los vuelos");
                Console.WriteLine("2. Buscar vuelos baratos por precio máximo");
                Console.WriteLine("3. Salir");
                Console.Write("Seleccione una opción: ");

                string opcion = Console.ReadLine();

                switch (opcion)
                {
                    case "1":
                        MostrarVuelos(vuelos);
                        break;
                    case "2":
                        BuscarVuelosBaratos(vuelos);
                        break;
                    case "3":
                        salir = true;
                        break;
                    default:
                        Console.WriteLine("Opción no válida. Presione Enter para continuar.");
                        Console.ReadLine();
                        break;
                }
            }
        }

        // Mostrar todos los vuelos
        static void MostrarVuelos(List<Vuelo> vuelos)
        {
            Console.Clear();
            Console.WriteLine("=== LISTA DE VUELOS ===");
            foreach (var vuelo in vuelos)
            {
                Console.WriteLine(vuelo);
            }
            Console.WriteLine("\nPresione Enter para regresar al menú.");
            Console.ReadLine();
        }

        // Buscar vuelos por precio máximo
        static void BuscarVuelosBaratos(List<Vuelo> vuelos)
        {
            Console.Clear();
            Console.Write("Ingrese el precio máximo: ");
            if (double.TryParse(Console.ReadLine(), out double precioMax))
            {
                var vuelosFiltrados = vuelos.FindAll(v => v.Precio <= precioMax);
                Console.WriteLine($"\nVuelos con precio hasta ${precioMax}:");
                if (vuelosFiltrados.Count == 0)
                {
                    Console.WriteLine("No se encontraron vuelos con ese precio.");
                }
                else
                {
                    foreach (var vuelo in vuelosFiltrados)
                    {
                        Console.WriteLine(vuelo);
                    }
                }
            }
            else
            {
                Console.WriteLine("Precio inválido.");
            }
            Console.WriteLine("\nPresione Enter para regresar al menú.");
            Console.ReadLine();
        }
    }
}
