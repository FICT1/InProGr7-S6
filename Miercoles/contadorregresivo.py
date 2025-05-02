#contador regresivo

import time
import os

def main():
    os.system("cls || clear")
    numero = int(input("Ingrese un número \n-> "))
    while numero >= 0:
        print(f"\rContando: {numero}        ", end="")
        time.sleep(1)
        numero -= 1
    print("\n¡Feliz año nuevo!")

main()
 
    