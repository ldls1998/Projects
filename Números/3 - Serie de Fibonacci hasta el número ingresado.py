import sys

# Aseguramos que si el programa no tiene el número de argumentos en la línea de comando correcto
# este mande un mensaje de error
if len(sys.argv) != 2:
    print("Ingrese un argumento.")
    exit()

# Primeros números de la serie de Fibonacci
primerNum = 0
segundoNum = 1

# Imprimimos los dos primeros números de la serie
print(f"{primerNum} {segundoNum} ", end="")

# Bucle que calcula los miembros de la serie hasta que el número sea mayor que el número ingresado en la línea de comandos
for i in range(int(sys.argv[1])):
    aux = primerNum + segundoNum
    primerNum = segundoNum
    segundoNum = aux
    if aux > int(sys.argv[1]):
        break
    print(aux, end=" ")
