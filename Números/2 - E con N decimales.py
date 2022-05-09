import math

try:
    while(True):
        n = int(input("Ingresa el número: "))
        if n > 0 and n <= 50:
            break
except ValueError:
    print("Ingresa un número.")
except:
    print("Ocurrió un error inesperado.")

# Número de epsilon (menor número sumado a 1 que de más que 1)
eps = 1.0
while eps + 1 > 1:
    eps /= 2
eps *= 2

print ("Pi con {num} decimales: {:.{num}f}".format(math.e, num = n))
