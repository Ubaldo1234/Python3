n = 5  # El número para calcular el factorial
resultado = 1
for i in range(1, n +1): #rango del 1,2,3,4,5
    resultado *= i
    """
    1x1=1
    1x2=2
    2x3=6
    6x4=24
    24x5=120
    esto se guarda en la variable resultado
    """

print("Factorial de", n, "es:", resultado)