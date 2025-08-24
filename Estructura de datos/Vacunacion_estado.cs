using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

class Program
{
    static void Main()
    {
        Random rand = new Random();

        // Conjunto universal de 500 pacientes
        HashSet<string> todos = new HashSet<string>(
            Enumerable.Range(1, 500).Select(i => $"Paciente {i}")
        );

        // Crear 75 vacunados con Pfizer
        HashSet<string> pfizer = new HashSet<string>();
        while (pfizer.Count < 75)
            pfizer.Add($"Paciente {rand.Next(1, 501)}");

        // Crear 75 vacunados con AstraZeneca
        HashSet<string> astrazeneca = new HashSet<string>();
        while (astrazeneca.Count < 75)
            astrazeneca.Add($"Paciente {rand.Next(1, 501)}");

        // Operaciones de conjuntos
        HashSet<string> vacunados = new HashSet<string>(pfizer);
        vacunados.UnionWith(astrazeneca);

        HashSet<string> noVacunados = new HashSet<string>(todos);
        noVacunados.ExceptWith(vacunados);

        HashSet<string> ambasDosis = new HashSet<string>(pfizer);
        ambasDosis.IntersectWith(astrazeneca);

        HashSet<string> soloPfizer = new HashSet<string>(pfizer);
        soloPfizer.ExceptWith(astrazeneca);

        HashSet<string> soloAstraZeneca = new HashSet<string>(astrazeneca);
        soloAstraZeneca.ExceptWith(pfizer);

        // --- Generar contenido del archivo ---
        List<string> lineas = new List<string>
        {
            "=== RESULTADOS CAMPAÑA DE VACUNACIÓN ===",
            "",
            $"Total pacientes: {todos.Count}",
            $"Pfizer: {pfizer.Count}, AstraZeneca: {astrazeneca.Count}",
            $"No vacunados: {noVacunados.Count}",
            $"Ambas dosis: {ambasDosis.Count}",
            $"Solo Pfizer: {soloPfizer.Count}",
            $"Solo AstraZeneca: {soloAstraZeneca.Count}",
            "",
            "---- LISTADOS COMPLETOS ----",
            "",
            "No vacunados: " + string.Join(", ", noVacunados),
            "Ambas dosis: " + string.Join(", ", ambasDosis),
            "Solo Pfizer: " + string.Join(", ", soloPfizer),
            "Solo AstraZeneca: " + string.Join(", ", soloAstraZeneca)
        };

        // --- Guardar archivo en la carpeta raíz del repositorio ---
        string rutaRepositorio = Directory.GetParent(Directory.GetCurrentDirectory()).Parent.Parent.FullName;
        string rutaArchivo = Path.Combine(rutaRepositorio, "resultados.txt");
        File.WriteAllLines(rutaArchivo, lineas);

        Console.WriteLine($"✅ Archivo 'resultados.txt' generado en: {rutaArchivo}");
    }
}
