numero1 = 20
numero2 = 0

#print("La división de {0} entre {1} es:".format(numero1,numero2,(numero1/numero2)))

try:
    resultado = numero1 / numero2
except ZeroDivisionError:
    print("No se puede dividir un numero entre 0")

finally:
    print("Fin del programa")