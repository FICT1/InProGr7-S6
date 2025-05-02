# Ejercicio 7: Número de dígitos
# Tipo de bucle: mientras
# Enunciado: Solicita un número positivo y cuenta cuántos dígitos tiene.
# Procedimiento paso a paso:
# 1. Solicita un número entero positivo.
# 2. Inicializa una variable de conteo de dígitos en 0.
# 3. Mientras el número sea mayor que 0:
# − Divide el número entre 10
# − Incrementa el conteo de dígitos.
# 4. Muestra la cantidad total de dígitos



# Ejercicio 7: Número de dígitos
import os
os.system("cls || clear")
print("**Número de dígitos**")
while True:
    numero = int(input("Ingrese un número entero positivo: "))
    if numero > 0:
        break
    print("El número debe ser positivo. Intente de nuevo.")
contador_digitos = 0
while numero > 0:
    numero = numero // 10
    contador_digitos += 1
print(f"La cantidad total de dígitos es: {contador_digitos}")
