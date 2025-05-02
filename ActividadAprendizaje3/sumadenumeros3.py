#Ejercicio 3: Suma de números hasta alcanzar un límite
#Tipo de bucle: repetir-hasta
#Enunciado: Solicita al usuario números hasta que la suma de ellos supere 100.
#Procedimiento paso a paso:
#1. Inicializa una variable suma en 0.
#2. Usa un bucle repetir-hasta para pedir al usuario que ingrese un número.
#3. Suma el número ingresado a la variable suma.
#4. Repite mientras la suma sea menor o igual a 100.
#5. Al finalizar, muestra la suma total.

print("**Suma de números hasta alcanzar un límite**")
import os
import time
os.system("cls || clear")
suma = 0
while True:
    numero = int(input("Introduce un número\n-> "))
    if numero < 0:
        print("El número debe ser positivo. Inténtalo de nuevo.")
        continue
    time.sleep(1)
    os.system("cls || clear")
    suma += numero
    if suma > 100:
        break
print(f"La suma total es: {suma}")

