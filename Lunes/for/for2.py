#la tabla de multiplicar de numero x
#def= (obtener_tabla)->nombre de funcion (numero)->parametro
#def guarda toda una funcion
#"for" es un ciclo
#|| significa o
import os
def obtener_tabla(numero):
    for i in range(13):
        print(f"{i} * {numero} = {i * numero}")

def main():
    os.system("cls || clear")
    number = int(input(f"Ingrese un #\n-> "))
    obtener_tabla(number)

main()
