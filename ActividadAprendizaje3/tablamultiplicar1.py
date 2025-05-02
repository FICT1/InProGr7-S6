# Ejercicio 1: Tabla de multiplicar
# Tipo de bucle: para
# Enunciado: Pide al usuario un número entero positivo y muestra su tabla de multiplicar del 1 al 10.
# Procedimiento paso a paso:
# 1. Solicita al usuario un número entero positivo.
# 2. Usa un bucle para que vaya de 1 a 10.
# 3. En cada iteración, multiplica el número ingresado por el número de la iteración.
# 4. Muestra el resultado en cada paso en pantalla.

import os
os.system("cls || clear")
numeroentero=int(input("Introduce un número entero positivo\n-> ")) 
for i in range(1,11):
    resultado=numeroentero*i
    print(f"{numeroentero} x {i} = {resultado}")
print("**Fin del programa**")
