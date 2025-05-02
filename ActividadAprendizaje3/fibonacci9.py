# Ejercicio 9: Serie de Fibonacci hasta un límite
# Tipo de bucle: para
# Enunciado: Genera los primeros n números de la serie de Fibonacci.
# Procedimiento paso a paso:
# 1. Solicita al usuario un número n (cantidad de elementos).
# 2. Inicializa las dos primeras variables de la serie en 0 y 1.
# 3. Usa un bucle para desde 1 hasta n.
# 4. En cada iteración:
# Muestra el valor actual
import os
import time

os.system("cls || clear")

print("***Serie de Fibonacci hasta un límite***")
n = int(input("Introduce un número entero positivo\n-> "))

fib1, fib2 = 0, 1

for i in range(1, n+1):
    if i == 1:
        fib = 0
    elif i == 2:
        fib = 1
    else:
        fib = fib1 + fib2
        fib1, fib2 = fib2, fib
    
    print(fib, end=" ")
    time.sleep(0.5)

print("\n***Fin del programa***")
print("¡Feliz fin de programa!")


