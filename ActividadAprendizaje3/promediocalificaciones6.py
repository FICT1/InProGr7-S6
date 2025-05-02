# Ejercicio 6: Promedio de calificaciones
# Tipo de bucle: repetir-hasta
# Enunciado: Solicita una cantidad indeterminada de calificaciones hasta que el usuario ingrese -1.
# Calcula y muestra el promedio.
# Procedimiento paso a paso:
# 1. Inicializa suma y contador en 0.
# 2. Usa un bucle repetir-hasta para pedir una calificación.
# 3. Si el número ingresado es diferente de -1, suma la calificación y aumenta el contador.
# 4. Finaliza cuando el usuario ingresa -1.
# 5. Calcula y muestra el promedio.

print ("**Promedio de calificaciones**")
import os
import time
os.system("cls || clear")
suma = 0
contador = 0
while True:
    calificacion = float(input("Introduce una calificación (-1 para terminar)\n-> "))
    if calificacion == -1:
        break
    suma += calificacion
    contador += 1
    time.sleep(0.5)
    os.system("cls || clear")
if contador > 0:
    promedio = suma / contador
    print(f"El promedio de las calificaciones es: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones válidas.")
