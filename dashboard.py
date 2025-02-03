import os
import subprocess

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

# Nueva función para crear carpetas
def crear_carpeta(ruta):
    nombre_carpeta = input("Ingrese el nombre de la nueva carpeta: ")
    nueva_ruta = os.path.join(ruta, nombre_carpeta)
    try:
        os.makedirs(nueva_ruta)
        print(f"Carpeta '{nombre_carpeta}' creada con éxito.")
    except FileExistsError:
        print("La carpeta ya existe.")
    except Exception as e:
        print(f"Error al crear la carpeta: {e}")

# Nueva función para eliminar carpetas vacías
def eliminar_carpeta(ruta):
    try:
        os.rmdir(ruta)
        print(f"Carpeta '{ruta}' eliminada con éxito.")
    except FileNotFoundError:
        print("La carpeta no existe.")
    except OSError:
        print("La carpeta no está vacía. No se puede eliminar.")
    except Exception as e:
        print(f"Error al eliminar la carpeta: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)
    unidades = {'1': 'Unidad 1', '2': 'Unidad 2'}

    while True:
        print("\nMenu Principal - Dashboard")
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("3 - Crear nueva unidad")  # Nueva opción para crear unidades
        print("0 - Salir")

        eleccion = input("Elige una opción: ")
        if eleccion == '0':
            print("Saliendo del programa.")
            break
        elif eleccion == '3':
            crear_carpeta(ruta_base)  # Llama a la nueva función de crear carpetas
        elif eleccion in unidades:
            ruta_unidad = os.path.join(ruta_base, unidades[eleccion])
            mostrar_sub_menu(ruta_unidad)
        else:
            print("Opción no válida.")

def mostrar_sub_menu(ruta_unidad):
    while True:
        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]
        print("\nSubmenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("C - Crear nueva subcarpeta")  # Nueva opción para crear subcarpetas
        print("D - Eliminar subcarpeta")  # Nueva opción para eliminar subcarpetas
        print("0 - Regresar al menú principal")

        eleccion = input("Elige una opción: ")
        if eleccion == '0':
            break
        elif eleccion.upper() == 'C':
            crear_carpeta(ruta_unidad)
        elif eleccion.upper() == 'D':
            carpeta_eliminar = input("Ingrese el nombre de la carpeta a eliminar: ")
            eliminar_carpeta(os.path.join(ruta_unidad, carpeta_eliminar))
        else:
            try:
                eleccion = int(eleccion) - 1
                if 0 <= eleccion < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion]))
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

def mostrar_scripts(ruta_sub_carpeta):
    while True:
        scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]
        print("\nScripts - Selecciona un script")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion == '0':
            break
        elif eleccion == '9':
            return
        else:
            try:
                eleccion = int(eleccion) - 1
                if 0 <= eleccion < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

if __name__ == "__main__":
    mostrar_menu()
