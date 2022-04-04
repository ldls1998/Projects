from math import pi 

try:
    while(True):
        n = int(input("Ingresa el número: "))
        if n > 0 and n <= 50:
            break
except ValueError:
    print("Ingresa un número.")
except:
    print("Ocurrió un error inesperado.")

print ("Pi con {num} decimales: {:.{num}f}".format(pi, num = n))
