# Ejercicio 8: Menú interactivo
# Tipo de bucle: repetir-hasta
# Enunciado: Implementa un menú con las opciones:
# 1. Saludar
# 2. Mostrar fecha
# 3. Salir
# El programa debe repetirse hasta que el usuario elija "Salir".
# Procedimiento paso a paso:
# 1. Mostrar un menú de opciones.
# 2. Solicitar al usuario su elección.
# 3. Usar un repetir-hasta para repetir mientras no elija "Salir".
# 4. Según la elección:
# − Opción 1: Mostrar un saludo
# − Opción 2: Mostrar la fecha actual
# − Opción 3: Terminar el programa

print ("**Menú Interactivo**")
import os
import time
import datetime
os.system("cls || clear")
opcion = 0
def main ():
    print("**Menú de opciones:**")
    print("1. Saludar")
    print("2. Mostrar fecha")
    print("3. Salir")
    print("**Fin del menú**")
main()
while opcion != 3:
    opcion = int(input("Elige una opción (1-3)\n-> "))
    os.system("cls || clear")
    if opcion == 1:
        print("¡Hola! ¿Cómo estás?")
        time.sleep(3)
        os.system("cls || clear")
        main()
    elif opcion == 2:
        fecha_actual = datetime.datetime.now()
        print(f"Fecha actual: {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(3)
        os.system("cls || clear")
        main()
    elif opcion == 3:
        print("¡Hasta luego!")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        time.sleep(3)
        os.system("cls || clear")

        main()
print("**Fin del programa**")
print("**Fin del menú**")
