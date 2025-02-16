import threading
import time

def tarea():
    print(f"Hilo {threading.current_thread().name} iniciado.")
    time.sleep(60)  # Cada hilo duerme durante 60 segundos
    print(f"Hilo {threading.current_thread().name} finalizado.")

# Crear 4 hilos
hilos = []
for i in range(4):
    hilo = threading.Thread(target=tarea, name=f"Hilo-{i+1}")
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("Todos los hilos han finalizado.")