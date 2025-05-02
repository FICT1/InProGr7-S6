# Ejercicio 4: Contador regresivo
# Tipo de bucle: para
# Enunciado: Solicita al usuario un número positivo e imprime un conteo regresivo hasta 0.
# Procedimiento paso a paso:
# 1. Solicita un número entero positivo.
# 2. Usa un bucle para que comience desde el número ingresado y vaya disminuyendo hasta 0.
# 3. Muestra cada número en pantalla.

import time
import os
os.system("cls || clear")
numeroentero=int(input("Cuantos segundos deseas? \n-> "))
while numeroentero >= 0:
    print(f"\rContando: {numeroentero}        ", end="")
    time.sleep(1)
    numeroentero -= 1
print("\n¡Feliz año nuevo!")
print("**Fin del programa**")
