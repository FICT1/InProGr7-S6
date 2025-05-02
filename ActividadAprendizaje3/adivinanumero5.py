# Ejercicio 5: Adivinar un número
# Tipo de bucle: mientras
# Enunciado: Genera un número aleatorio entre 1 y 10. El usuario debe adivinarlo. El programa da
# pistas: "mayor" o "menor".
# Procedimiento paso a paso:
# 1. Genera un número aleatorio entre 1 y 10.
# 2. Solicita al usuario que ingrese un número.
# 3. Mientras el número ingresado sea diferente al número generado:
# − Informa si debe intentar con un número mayor o menor
# − Pide un nuevo número
# 4. Felicita al usuario al adivinarlo

print("**Adivina el número**")
import os
import random
os.system("cls || clear")
numero_aleatorio = random.randint(1, 10)
numero_usuario = int(input("Adivina el número entre 1 y 10\n-> "))
while numero_usuario != numero_aleatorio:
    if numero_usuario < numero_aleatorio:
        print("***Intenta con un número mayor***.")
    else:
        print("***Intenta con un número menor***.")
    numero_usuario = int(input("Intenta de nuevo del 1 y 10\n-> "))
    os.system("cls || clear")
print(f"¡Felicidades! Adivinaste el número ({numero_aleatorio}).")
print("**Fin del programa**")
