import os
import time

def listar_archivos():
    archivos = [f for f in os.listdir() if f.endswith(".txt")]
    return archivos

def elegir_archivo():
    archivos = listar_archivos()
    
    if not archivos:
        print("No hay archivos .txt en la carpeta")
        return None
    print("Archivos disponibles: \n")
    for i, archivo in enumerate(archivos, start=1):
        print(f"{i}, {archivo}")

    opcion = input("\n Elige un número: ")

    try:
        indice = int(opcion) - 1
        return archivos[indice]
    except:
        print("Opción invalida")
        return None



def menu():
    print(f"Escoge el tipo de animación \n")
    print(f"1. Linea por linea")
    print(f"2. Maquina de escribir")

# Limpiar la consola
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Maquina de escribir
def maquina(arte, delay=0.002):
    for char in arte:
        print(char, end="", flush=True)
        time.sleep(delay)

# Linea x linea 
def animar_linea(text, delay=0.1):
    lineas = text.split("\n")
    output = ""

    for linea in lineas:
        output += linea + "\n"
        clear()
        print(output)
        time.sleep(delay)


# Entrada
archivo = elegir_archivo()

if archivo:
    with open(archivo, "r", encoding="utf-8") as f:
        ascii_art = f.read()
else:
    exit()

menu()
opcion = input("Escoge una opción: ")

if opcion == "1":
   animar_linea(ascii_art) 
elif opcion == "2":
    maquina(ascii_art)

